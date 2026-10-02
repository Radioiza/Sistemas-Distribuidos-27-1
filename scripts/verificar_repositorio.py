"""Comprobaciones de entrega. No reemplaza revisión visual ni prueba de cuentas."""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    'AWS access key': re.compile(rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    'GitHub token': re.compile(rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bgithub_pat_[A-Za-z0-9_]{40,}\b'),
    'Private key': re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'Google API key': re.compile(rb'\bAIza[A-Za-z0-9_-]{35}\b'),
    'AWS secret assignment': re.compile(rb'(?i)aws_secret_access_key\s*[=:]\s*[\"\x27]?[A-Za-z0-9/+=]{40}'),
}

def forbidden(name):
    p = Path(name)
    return ((p.name == '.env' or p.name.startswith('.env.')) and p.name != '.env.example'
            or p.suffix.lower() in {'.pem', '.key', '.pfx', '.p12'}
            or p.suffix.lower() == '.json' and any(s in p.name.lower() for s in ('credentials', 'service-account')))

def scan(data, label):
    return [f'{label}: posible {kind} (valor omitido)' for kind, pattern in PATTERNS.items() if pattern.search(data)]

def git(*args):
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True)

def main():
    errors = []
    files = [p for p in ROOT.rglob('*') if p.is_file() and not any(x in {'.git', '.venv', '__pycache__', 'tmp'} for x in p.relative_to(ROOT).parts)]
    for p in files:
        rel = p.relative_to(ROOT)
        if forbidden(rel):
            errors.append(f'{rel}: nombre de archivo prohibido')
        if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.pdf', '.xlsx', '.zip'}:
            continue
        data = p.read_bytes()
        errors.extend(scan(data, str(rel)))
        if p.suffix.lower() == '.md':
            body = data.decode('utf-8-sig')
            for href in re.findall(r'\]\(([^\s)]+)\)', body):
                if re.match(r'^[a-zA-Z][\w+.-]*:', href) or href.startswith('#'):
                    continue
                target = unquote(href.split('#')[0])
                if target and not (p.parent / target).exists():
                    errors.append(f'{rel}: enlace local inexistente: {target}')
    for required in ['README.md', 'practicas/P01/README.md', 'evidencias/P01/README.md', 'bitacora/2026-09-01.md', 'bitacora/2026-09-08.md', 'bitacora/2026-10-01.md']:
        if not (ROOT / required).is_file():
            errors.append(f'Falta archivo obligatorio: {required}')
    commits = git('rev-list', '--all')
    if commits.returncode:
        errors.append('No se pudo inspeccionar el historial Git')
    seen = set()
    for commit in commits.stdout.decode().splitlines():
        tree = git('ls-tree', '-rz', commit)
        if tree.returncode:
            errors.append('No se pudo leer un árbol del historial')
            continue
        for item in tree.stdout.split(b'\0'):
            if not item:
                continue
            meta, filename = item.split(b'\t', 1)
            mode, kind, oid = meta.split()
            name = filename.decode('utf-8', errors='replace')
            if forbidden(name):
                errors.append(f'Historial {commit[:8]}: archivo prohibido {name}')
            if kind == b'blob' and oid not in seen:
                seen.add(oid)
                blob = git('cat-file', 'blob', oid.decode())
                if blob.returncode:
                    errors.append('No se pudo leer contenido del historial')
                else:
                    errors.extend(scan(blob.stdout, f'Historial {commit[:8]} / {name}'))
    for error in sorted(set(errors)):
        print('ERROR:', error)
    print(f'Archivos revisados: {len(files)}; objetos históricos: {len(seen)}; incidencias: {len(set(errors))}')
    print('Las imágenes y los documentos binarios requieren revisión visual. Esto no verifica cuentas ni presupuestos.')
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
