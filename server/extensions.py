from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.principal import Principal
from flask.ext.security import Security

babel = Babel()
mail = Mail()
db = SQLAlchemy()
principal = Principal()
security = Security()
