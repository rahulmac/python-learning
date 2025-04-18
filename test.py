import sys

class One:
    def __init__(self):
        print('contrroller')    
    
    def name(self):
        print('this is the user name rahul')    

class Two(One):
    def __init__(self):
        print('class two')
        
obj = Two()
obj.name()