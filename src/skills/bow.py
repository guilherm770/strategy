from .interface import Iskill

class Bow(Iskill):

    def __init__(self, level):
        self.level = level
    
    def behave(self):
        print("Shooting Arrows")
    
    def attr_level(self):
        print('Bow Level: {}'.format(self.level))