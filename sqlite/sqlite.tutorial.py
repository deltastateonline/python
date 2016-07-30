# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 06:42:24 2016

@author: developer
"""
import sqlite3
# Calls the above functions with interesting inputs.
def main():
    
    renderMenu()
    
    options = {
        "X":deleteDatabase,
        "C":createDatabase,
        "I":insertRecord,
        "R":readRecords,
        "F":findRecord,
        "D":delRecord
        
    }    
    
    db = sqlite3.connect('data/mydb.sqlite') 
    
    doWhat = "";
   
    while doWhat != "Q":
        doWhat = readInput()
        doWhat = doWhat.upper()
        if doWhat in options.keys():
            options[doWhat](db)        
    
    db.close()
    
def renderMenu():
    print """**********************************
    (C)reate Database ..   
    (D)elete Record ..  
    (F)ind Records ..  
    (I)nsert Records ..  
    (R)ead Records..
    (Q)uit Program ..
    (X)elete Database ..  
**********************************"""
    

def readInput():
    act = input("What action do you want to perform ? ")
    return act
    
def readDetails():
    carDetails = input("Enter the Car Details as 'make,price' ? ")
    x,y = carDetails.split(",")
    return {"carMake":x,"price":float(y)}
    
def createDatabase(db):
    # Get a cursor object
    print "Creating Database ...."
    try:
       
    except BaseException:
        print("Something went wrong!  Try again...")
    
    
def deleteDatabase(db):
    # Get a cursor object
    print "Deleting Database ...."
    try:
       
    except BaseException:
        print("Something went wrong!  Try again...")
    
def insertRecord(db):
      # Get a cursor object
    print "Insert Records ...."
    try:
       
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
    

def readRecords(db):
    print "Reading Records ...."
    try:
       
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
   

def findRecord(db):
    print "Finding a record.."
    carMake = input("Enter the Car Make..")
    try:
        
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
 
 
def delRecord(db):
    print "Delete a record.."
    carMake = input("Enter the Car Make..")
    try:
        
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")   
    

if __name__ == '__main__':
    main()
