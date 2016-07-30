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
            print "%4d %s\t| %10.2f"%(x["id"],x["carMake"],x["price"])
           
               
        db.commit()
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
   

def findRecord(db):
    print "Finding a record.."
    carMake = input("Enter the Car Make..")
    try:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
       
        cursor.execute('''select * from carlist where carMake like ?''',('%'+carMake+'%',))                       
        allRecords = cursor.fetchall()
        if allRecords :
        	for x in allRecords:
        		print "%4d  %s\t| %10.2f"%(x["id"],x["carMake"],x["price"])
        else:
         	 print "Unable to find record for search term {0}".format(carMake)
               
        db.commit()
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")
 
 
def delRecord(db):
    print "Delete a record.."
    carMake = input("Enter the Car Make..")
    try:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
       
        cursor.execute('''select * from carlist where carMake like ?''',('%'+carMake+'%',))                      
        allRecords = cursor.fetchall()
        if allRecords :
        	for x in allRecords:
        		print "%4d  %s\t| %10.2f"%(x["id"],x["carMake"],x["price"])
        		deleteRec = input("Delete? (Y)es or (N)o ..")
        		if(deleteRec.upper() == "Y"):
        			cursor.execute('''delete from carlist where id = ?''',(x["id"],)) 
        else:
         	 print "Unable to find record for search term {0}".format(carMake)
               
        db.commit()
    except BaseException as inst:
        print inst
        print("Something went wrong!  Try again...")   
    

if __name__ == '__main__':
    main()
