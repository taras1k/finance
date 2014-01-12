import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'e31c6de09428e55753ce30c9c17ba2c7'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
DEBUG = True

#static urls
JQUERY_CDN_URL = '//ajax.googleapis.com/ajax/libs/jquery/'


RESET_EXPIRE_MINUTES = 60
USER_LICENSE_EXPIRE_DAYS = 365

#Flask Security
SECURITY_LOGIN_USER_TEMPLATE = 'account/login.html'

#mail config
#DEFAULT_MAIL_SENDER
#MAIL_SERVER
#MAIL_PORT
#MAIL_USE_TLS : default False
#MAIL_USE_SSL
#MAIL_DEBUG : default app.debug
#MAIL_USERNAME
#MAIL_PASSWORD

LOG_FILE = '%s/app.log' % basedir
WSGI_SCRIPT = '%s/app.sock' % basedir

