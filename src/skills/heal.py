from .interface import Iskill

class Heal(Iskill):

    def __init__(self, level):
        self.level = level
    
    def behave(self):
        print("Healing")
    
    def attr_level(self):
        print('Healing Level: {}'.format(self.level))