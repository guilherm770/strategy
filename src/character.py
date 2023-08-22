from typing import Type
from .skills import Iskill

class Character:
    
    def __init__(self, skill: Type[Iskill]):
        self.skill = skill
    
    def action(self):
        self.skill.behave()
    
    def attr(self):
        self.skill.attr_level()