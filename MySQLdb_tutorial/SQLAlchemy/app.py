#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)

engine = create_engine('sqlite://:memory:', echo=True)
Base.meta