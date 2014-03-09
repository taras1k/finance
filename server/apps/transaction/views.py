from flask import Blueprint, jsonify, request
from extensions import db
from .models import Transaction

transaction_api = Blueprint('transaction', __name__)


@transaction_api.route('/', methods=['GET'])
def get_all():
    objects = db.session.query(Transaction).all()
    data = {}
    data['objects'] = [ob._asdict() for ob in objects]
    return jsonify(data)

@transaction_api.route('/', methods=['POST'])
def save_transaction():
    data = request.get_json()
    if data.get('amount', '') == '':
        errors = {'amount': 'field is required'}
        return jsonify(errors), 400
    transaction = Transaction()
    transaction.amount = data['amount']
    db.session.add(transaction)
    db.session.commit()
    return jsonify(transaction._asdict()), 201
