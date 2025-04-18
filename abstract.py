from abc import ABC, abstractmethod

class Animal(ABC):
    def name(self):
        print('elephant')
    @abstractmethod
    def color(self):
        
obj = Animal()
obj.name()