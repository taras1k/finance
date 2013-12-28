from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.principal import Principal

babel = Babel()
mail = Mail()
db = SQLAlchemy()
principal = Principal()
