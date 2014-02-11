from flask import Flask, render_template
from flask.ext.security import SQLAlchemyUserDatastore, login_required
from extensions import babel, mail, db, principal, security, api_manager
from apps.account.models import User, Role
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')

babel.init_app(app)
mail.init_app(app)
db.init_app(app)
db.app = app
principal.init_app(app)
api_manager.init_app(app, flask_sqlalchemy_db=db)
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security.init_app(app, datastore=user_datastore)
security.datastore = user_datastore
Bootstrap(app)

api_manager.create_api(User, methods=['GET'])

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
