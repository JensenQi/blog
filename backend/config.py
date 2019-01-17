from configparser import ConfigParser
from os import path

cf = ConfigParser()
cf.read(path.join(path.dirname(__file__), 'config.ini'))

HOST = cf.get('webserver', 'host')
PORT = cf.get('webserver', 'port')
SECRET_KEY = cf.get('webserver', 'secret_key')

ROOT_NAME = cf.get('webserver', 'root_name')
ROOT_PASSWD = cf.get('webserver', 'root_passwd')

LOG_PATH = cf.get('webserver', 'log_path')
DB_URI = cf.get('db', 'uri')
