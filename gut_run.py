import argparse

from gut.init import init
from gut.hash import hash_object

parser = argparse.ArgumentParser()
parser.add_argument('--hash_object', action="store", nargs=2)
parser.add_argument('--init', action="store")
args = parser.parse_args()

if args.init:
  init()

if args.hash_object:
  type, filepath = args.hash_object
  hash_object(hash_type=type,
              filepath=filepath)
