from .interface import Iskill

class Ax(Iskill):

    def __init__(self, level):
        self.level = level
    
    def behave(self):
        print("Fighting with ax")
    
    def attr_level(self):
        print('Ax Level: {}'.format(self.level))