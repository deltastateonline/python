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
        "C":createDatabase
    }    
    
    db = sqlite3.connect('data/mydb') 
    
    doWhat = "";
    #createDatabase(db)
    while doWhat != "Q":
        doWhat = readInput()
        if doWhat in options.keys():
            options[doWhat](db)        
    
    db.close()
    
def renderMenu():
    print """**********************************
    (C)reate Database ..   
    (D)elete Database ..   
    (Q)uit Program ..   
**********************************"""
    

def readInput():
    act = input("What action do you want to perform ? ")
    return act
    
def createDatabase(db):
    # Get a cursor object
    print "Creating Database ...."
    try:
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                               phone TEXT, email TEXT unique, password TEXT)
        ''')
        db.commit()
    except BaseException:
        print("Something went wrong!  Try again...")
    
    
def deleteDatabase(db):
    # Get a cursor object
    print "Deleting Database ...."
    try:
        cursor = db.cursor()
        cursor.execute('''DROP TABLE users''')
        db.commit()
    except BaseException:
        print("Something went wrong!  Try again...")
    


if __name__ == '__main__':
    main()
