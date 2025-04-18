import sys

class flats:
    def name(self):
        print("name is rajipa")
    
    def year(self):
        print("flat was built in year 2007")
        
class flat1(flats):
    def name(self):
        print("name is silverheight")
        

obj = flat1()
obj.name()
obj.year()