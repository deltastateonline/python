class Fridge:
    def __init__(self, items={}):
        """Optionally pass in an initial dictionary of items"""
        if type(items) != type({}):
            raise TypeError, "Fridge requires a dictionary but was given %s" %type(items)
        self.items = items
        return
    def __add_multi(self,foodname,qty):        
        self.items[foodname] = self.items.get(foodname,0)+qty;        
        return
    
    def add_one(self,foodname):
        self.__add_multi(foodname,1)
        return
    def add_many(self,fooddict):
        
        if(type(fooddict) != type({})):
            raise TypeError, "add_many requires a dictionary, got a %s" % food_dict
        for x in fooddict.keys():
            self.__add_multi(x,fooddict[x])
        return
    def has(self,foodname,qty=1):        
        return self.has_various({foodname:qty})
    def has_various(self,fooddict):
        try:
            for x in fooddict.keys():
                if(fooddict[x] > self.items[x]):
                    return False
                
            return True
        except KeyError:
            return False
     
    def __str__(self):
        i = 1;
        print "+=======Fridge Content==========+"        
        for x in sorted(self.items):
            print "%3d : %s\t: $%10.2f"%(i,x.capitalize(),self.items[x])
            i= i+1
        print "+===============================+"
        return ""
