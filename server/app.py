from flask import Flask, render_template
from extensions import babel, mail, db, principal

app = Flask(__name__)
app.config.from_object('config')

babel.init_app(app)
mail.init_app(app)
db.init_app(app)
db.app = app
principal.init_app(app)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
