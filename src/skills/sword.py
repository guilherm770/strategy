from .interface import Iskill

class Sword(Iskill):

    def __init__(self, level):
        self.level = level
    
    def behave(self):
        print("Sword Fighting")
    
    def attr_level(self):
        print('Sword Level: {}'.format(self.level))