from sqlalchemy import Column, String, Integer, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, backref
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column (Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = Column(String, primary_key=True)
    last_name = Column(String, primary_key=True)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
    birth_date = Column(String)


class ParentChild(Base):
    __tablename__ = 'parentchild'
    __table_args__ = (CheckConstraint("parent <> child"),)
    id = Column(Integer, primary_key=True, autoincrement=True)
    parent = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    child = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    person = relationship("Persons", backref=backref("parentchild", cascade="all, delete-orphan", passive_deletes=True),)

    




