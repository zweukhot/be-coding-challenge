from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column (Integer, primary_key=True)
    first_name = Column(String, primary_key=True)
    last_name = Column(String, primary_key=True)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
    birth_date = Column(String)


class ParentChild(Base):
    __tablename__ = 'parents'
    parent = Column(Integer, primary_key=True)
    child = Column(Integer, primary_key=True)




