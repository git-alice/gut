from gut.utils import sha1sum, save_file

def hash_object(hash_type: str, filepath: str):
  hash_file = sha1sum(filepath)
  save_file(hash_file, hash_type)
  print(f'{filepath} -> {hash_type} {hash_file}')
