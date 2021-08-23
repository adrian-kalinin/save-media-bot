from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')


# project section
DEBUG = config.getboolean('project', 'debug')

# bot section
BOT_TOKEN = config.get('bot', 'token')
ADMINS = tuple(map(int, config.get('bot', 'admins').split(', ')))
DEVELOPER = config.getint('bot', 'developer')
CHANNEL = config.get('bot', 'channel')

# database section
DATABASE_PATH = config.get('database', 'sqlite')

# server section
LISTEN = config.get('server', 'listen')
HOST = config.get('server', 'host')
PORT = config.getint('server', 'port')

# webhook section
WEBHOOK_URL = config.get('webhook', 'webhook_url')
KEY_PATH = config.get('webhook', 'key_path')
CERT_PATH = config.get('webhook', 'cert_path')

# instagram section
INSTAGRAM_USERNAME = config.get('instagram', 'username')
INSTAGRAM_PASSWORD = config.get('instagram', 'password')
