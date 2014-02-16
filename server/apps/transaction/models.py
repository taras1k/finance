from extensions import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))
    owner = db.relationship('User',
                            backref=db.backref('transactions', lazy='dynamic'))
