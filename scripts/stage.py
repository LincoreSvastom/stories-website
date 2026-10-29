"""Stage only the public allowlist. Never deploy the repository root."""
from pathlib import Path
import shutil
import sys
from validate import ROOT,PUBLIC_FILES,validate

validate('--publish' in sys.argv)
target=ROOT/'_site'
target.mkdir(exist_ok=True)
if target.resolve().parent!=ROOT.resolve():raise RuntimeError('Unsafe staging directory')
if any(p.name not in PUBLIC_FILES or not p.is_file() or p.is_symlink() for p in target.iterdir()):
    raise RuntimeError('Unexpected staging contents; refusing to publish')
for name in PUBLIC_FILES:
    source=ROOT/name
    if source.is_symlink():raise RuntimeError('Symlink rejected')
    shutil.copyfile(source,target/name)
print('Staged allowlisted assets in _site/ only.')
