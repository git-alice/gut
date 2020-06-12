import configparser

config = configparser.ConfigParser()
config.read('config.ini')

root = config.get('APP', 'ROOT')
debug = config.get('APP', 'DEBUG')
