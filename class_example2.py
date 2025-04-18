import sys

class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        
    def car_info(self):
        print("Car "+self.name + " and model "+ self.model + " is build on year "+self.year)
        

car1 = Car("Tata", "Nexon", "2019")
car1.car_info()