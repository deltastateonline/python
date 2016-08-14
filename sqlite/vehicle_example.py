# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:17:18 2016

@author: developer
"""

from vehicle_declare import Vehicle, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


def main():
    
    renderMenu()
    
    options = {
        "X":deleteDatabase,
        "C":createDatabase,
        "I":insertRecord,
        "R":readRecords,
        "F":findRecord,
        "D":delRecord,
        "V":versionCheck
        
    }    
    
    engine = create_engine("sqlite:////home/developer/python/sqlite/data/carlist.sqlite")

    Base.metadata.bind = engine
    
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
    
    doWhat = "";
   
    while doWhat != "Q":
        doWhat = readInput()
        doWhat = doWhat.upper()
        if doWhat in options.keys():
            options[doWhat](session)        
    

def renderMenu():
    print """**********************************
    (C)reate Database \t..   
    (D)elete Record\t ..  
    (F)ind Records\t ..  
    (I)nsert Records\t ..  
    (R)ead Records\t..
    (Q)uit Program \t..
    (V)ersion Check \t..
    (X)elete Database \t..  
**********************************"""
    

def readInput():
    act = raw_input("What action do you want to perform ? ")
    return act


def versionCheck(session):
    print sqlalchemy.__version__   

def readRecords(session):
    print "Reading Records ...."
    try:
       allVehicles = session.query(Vehicle).all()
       print """+=========================================+"""
       for a in allVehicles:
            a.render()
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")

def findRecord(session):
    print "Finding a record.."
    carMake = raw_input("Enter the Car Make..")
    print """+=========================================+"""
    try:
        carMake = "%"+carMake+"%"
        single = session.query(Vehicle).filter(Vehicle.carMake.like(carMake)).one()
        single.render()
    except NoResultFound as inst:
        print inst
    except MultipleResultsFound as inst:
         print inst
    
    print """+=========================================+"""    
   

def deleteDatabase(session):
    print "Delete Database"
    
def createDatabase(session):
    print "Create Database"
    
def insertRecord(session):
    print "Insert New Record"
    try:
        carMake, price = raw_input("Enter Car details as car name,price > ").split(',')
        new_car = Vehicle(carMake=carMake, price=float(price))       
        session.add(new_car)
        session.commit()
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
        
        
 
def delRecord(session):
    print "Delete Record"

if __name__ == '__main__':
    main()
  