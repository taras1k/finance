from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users_transactions = Table('users_transactions', post_meta,
    Column('user_id', Integer),
    Column('transaction_id', Integer),
)

transaction = Table('transaction', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('amount', Numeric(precision=10, scale=2)),
    Column('owner_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['users_transactions'].create()
    post_meta.tables['transaction'].columns['owner_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['users_transactions'].drop()
    post_meta.tables['transaction'].columns['owner_id'].drop()
