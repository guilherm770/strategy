from abc import ABC, abstractclassmethod

class Iskill(ABC):

    @abstractclassmethod
    def behave(self):
        pass
    
    @abstractclassmethod
    def attr_level(self):
        pass