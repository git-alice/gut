import configparser

config = configparser.ConfigParser()
config.read('config.ini')

root = config.get('APP', 'ROOT')
objects = config.get('APP', 'OBJECTS')
