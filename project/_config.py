import os

#grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))


DATABASE = 'flasktaskr.db'

USERNAME = 'admin'

PASSWORD = 'admin'

WTF_CSRF_ENABLED = True

SECRET_KEY = '8d45f51a8944e956bdfc59c431184d769cdc775f7a8e7c1c16b09b0c8d6625f3'

DATABASE_PATH = os.path.join(basedir, DATABASE)