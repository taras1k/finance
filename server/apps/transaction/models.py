from extensions import db
from utils import SerializableModel

users_transactions = db.Table('users_transactions',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('transaction_id', db.Integer(), db.ForeignKey('transaction.id')))

class Transaction(db.Model, SerializableModel):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    owner = db.relationship('User', backref='transactions')


