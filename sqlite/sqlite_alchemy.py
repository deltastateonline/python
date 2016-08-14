# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:26:21 2016

@author: developer
"""

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import  create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code =  Column(String(250),nullable=False)
    persone_id = Column(Integer,ForeignKey('person.id'))
    person = relationship(Person)

class Contact(Base):
    __tablename__ = 'contactdetails'
    id = Column(Integer, primary_key=True)
    detail_type = Column(String(250))
    detail_value = Column(String(250))   
    persone_id = Column(Integer,ForeignKey('person.id'))
    person = relationship(Person)

engine = create_engine("sqlite:////home/developer/python/sqlite/data/person.sqlite")

Base.metadata.create_all(engine)