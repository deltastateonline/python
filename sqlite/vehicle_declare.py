# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:45:02 2016

@author: developer
"""

import os
import sys
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import  create_engine


Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'carlist'
    id = Column(Integer, primary_key=True)
    carMake = Column(String(250),nullable=False)
    price = Column(Numeric)
    
    def render(self):
        print "%d\t%s\t%10.2f"%(self.id,self.carMake,self.price) 
    
    
engine = create_engine("sqlite:////home/developer/python/sqlite/data/carlist1.sqlite")

Base.metadata.create_all(engine)