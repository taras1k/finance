import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
DEBUG = True

#static urls
JQUERY_CDN_URL = '//ajax.googleapis.com/ajax/libs/jquery/'


RESET_EXPIRE_MINUTES = 60
USER_LICENSE_EXPIRE_DAYS = 365

#Flask Security
SECURITY_LOGIN_USER_TEMPLATE = 'account/login.html'
SECURITY_REGISTER_USER_TEMPLATE = 'account/register_user.html'
SECURITY_REGISTERABLE = True
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

