import hashlib
from pathlib import Path
import zlib

from gut.settings import root, objects

def sha1sum(filepath: str) -> str:
    hash = hashlib.sha1()
    with open(filepath, mode="rb") as f:
        hash.update(f.read())
    return hash.hexdigest()

def save_file(filepath, filehash, filetype):
  raw_filename = filehash

  if filetype == 'blob':
    to_dir = Path(root) / Path(objects)
    
  filedir, filename = Path(raw_filename[:2]), Path(raw_filename[2:])
  (to_dir / filedir).mkdir(parents=True, exist_ok=True)
  (to_dir / filedir / filename).touch()

  original_data = open(filepath, 'rb').read()
  compressed_data = zlib.compress(original_data)

  with open(to_dir / filedir / filename, 'wb') as f:
    f.write(compressed_data)
  
  # print(f'Orginal data: {original_data}')
  # print(f'Compressed data: {compressed_data}')
