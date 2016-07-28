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
        "D":deleteDatabase,
        "C":createDatabase,
        "I":insertRecord,
        "R":readRecords
    }    
    
    db = sqlite3.connect('data/mydb.sqlite') 
    
    doWhat = "";
    #createDatabase(db)
    while doWhat != "Q":
        doWhat = readInput()
        doWhat = doWhat.upper()
        if doWhat in options.keys():
            options[doWhat](db)        
    
    db.close()
    
def renderMenu():
    print """**********************************
    (C)reate Database ..   
    (D)elete Database ..  
    (I)nsert Records ..  
    (R)ead Records
    (Q)uit Program ..   
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
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE carlist(id INTEGER PRIMARY KEY, carMake TEXT,price real)
        ''')
        db.commit()
    except BaseException:
        print("Something went wrong!  Try again...")
    
    
def deleteDatabase(db):
    # Get a cursor object
    print "Deleting Database ...."
    try:
        cursor = db.cursor()
        cursor.execute('''DROP TABLE carlist''')
        db.commit()
    except BaseException:
        print("Something went wrong!  Try again...")
    
def insertRecord(db):
      # Get a cursor object
    print "Insert Records ...."
    try:
        cursor = db.cursor()
        carData = readDetails()
        print carData
        cursor.execute('''INSERT INTO carlist(price,carMake)
                  VALUES(:price,:carMake)''',carData)                       
                        
        db.commit()
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
    

def readRecords(db):
    print "Reading Records ...."
    try:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
       
        cursor.execute('''select * from carlist''')                       
        allRecords = cursor.fetchall()
        for x in allRecords:
            print "%s\t| %.2f"%(x["carMake"],x["price"])
           
               
        db.commit()
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
    
    

if __name__ == '__main__':
    main()
