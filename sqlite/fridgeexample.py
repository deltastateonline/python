from fridgeclass import Fridge

def main():
    
    renderMenu()
    
    myFridge = Fridge({})
    
    options = {       
        "I":insertRecord,
        "R":readRecords,
        "F":findRecord,
        "D":delRecord,
        
    }    
    
    
    
    doWhat = "";
   
    while doWhat != "Q":
        doWhat = readInput()
        doWhat = doWhat.upper()
        if doWhat in options.keys():
            try:
                options[doWhat](myFridge)
            except BaseException as inst:
                print inst
                print("Something went wrong!  Try again...")
    
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

def insertRecord(myFridge):
     itemName, itemQty = raw_input("Enter Shopping Item Details <item name,item qty > ").split(',')
    
     myFridge.add_many({itemName:int(itemQty)})
     return
    
def readRecords(myFridge):
    print myFridge
    return
def findRecord(myFridge):
    return
    
def delRecord(myFridge):
    return




    
    
if __name__ == '__main__':
    main()