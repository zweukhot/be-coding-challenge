from sqlalchemy import Column, String, Integer, CheckConstraint, UniqueConstraint
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
    __table_args__ = (CheckConstraint("parent_id <> child_id"), UniqueConstraint("parent_id", "child_id"))
    parent_id = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    child_id = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
    child = relationship("Person", foreign_keys=[child_id])
    parent = relationship("Person", foreign_keys=[parent_id])
    




