import argparse

from gut.init import init

parser = argparse.ArgumentParser()
parser.add_argument('init', help='init help')
args = parser.parse_args()

if 'init' in args:
    init()
