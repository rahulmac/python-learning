import sys

class User:
    def __init__(self ,name, age, number):
        self.name = name
        self.age = age
        self.number = number
        
    def userProfile(self):
        print(self.name + " is " + self.age + " years old and his phone number is "+self.number)
        
userProfile1 = User("Rahul", "21", "8469681300")
userProfile1.userProfile()