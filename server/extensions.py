from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.principal import Principal
from flask.ext.security import Security
import flask.ext.restless

babel = Babel()
mail = Mail()
db = SQLAlchemy()
principal = Principal()
security = Security()
api_manager = flask.ext.restless.APIManager(flask_sqlalchemy_db=db)
