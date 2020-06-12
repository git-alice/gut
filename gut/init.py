from pathlib import Path

from gut import settings

def init():
  init_dirs = map(Path, ['objects', 'refs', 'refs/heads'])
  for init_dir in init_dirs:
    (Path(settings.root) / init_dir).mkdir(parents=True, exist_ok=True)
  with open(Path(settings.root) / 'HEAD', 'wb') as f:
    f.write(b'ref: refs/heads/master')
  print('Inited empty repository.')
