import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#connect with database
engine = create_engine('sqlite:///:memory:', echo=True)

#manage tables
base = declarative_base()

class transactions(base):
    __tablename__ = 'transactions'

    transactions_id = Column(Integer, primary_key=True)
    date = Column(String)
    item_id = Column(Integer)
    price = Column(Integer)

def __init__(self,transaction_id,date,item_id,price):
    self.transaction_id = transaction_id
    self.date = date
    self.item_id = item_id
    self.price = price

base.metadata.create_all(engine)