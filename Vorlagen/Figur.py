import pgzrun
from pgzhelper import *

class Figur(Actor):
    def __init__(self, x, y):
        super().__init__('BildDatei')
        self.aktiv = False 
        # Die aktuelle Position
        self.x = x
        self.y = y

    def start(self):
        self.aktiv = True
        
    def stopp(self):
        self.aktiv = False

    def kollision(self):
        self.stopp()

    def update(self):
        if not self.aktiv: return
        