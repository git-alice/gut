import hashlib
from pathlib import Path

from gut.settings import root, objects

def sha1sum(filepath: str) -> str:
    hash = hashlib.sha1()
    with open(filepath, mode="rb") as f:
        hash.update(f.read())
    return hash.hexdigest()

def save_file(filehash, type):
  raw_filename = filehash
  if type == 'blob':
    to_dir = Path(root) / Path(objects)
  filedir, filename = Path(raw_filename[:2]), Path(raw_filename[2:])
  (to_dir / filedir).mkdir(parents=True, exist_ok=True)
  (to_dir / filedir / filename).touch()
