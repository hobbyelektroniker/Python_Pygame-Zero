'''
  Gameprogrammierung mit Python und Pygame Zero
  Version 1.00, 23.09.2021
  Der Hobbyelektroniker
  https://community.hobbyelektroniker.ch
  https://www.youtube.com/c/HobbyelektronikerCh
  Die Rechte der unten angegebenen Quellen sind zu beachten!
  Der restliche Code kann mit Quellenangabe frei verwendet werden.
  
  - Als Entwicklungsumgebung wird Thonny verwendet: https://thonny.org
  - Die Ideen zu diesem Tutorial stammt von https://aposteriori.trinket.io/game-development-with-pygame-zero
  - Grafiken von https://www.aposteriori.com.sg/wp-content/uploads/2020/02/image_pack.zip
  - Sounds von https://opengameart.org
  - Das Modul pgzhelper:https://www.aposteriori.com.sg/wp-content/uploads/2021/01/pgzhelper.zip
  - Tool zur Bestimmung der Farbwerte:https://www.rapidtables.com/web/color/RGB_Color.html 
  - Dokumentation zu Pygame Zero: https://pygame-zero.readthedocs.io/en/stable/
'''

import pgzrun
from pgzhelper import *

class Hindernis(Actor):
    def __init__(self, x, y):
        super().__init__('cactus')
        self.aktiv = False
        self.scale = 2
        # Die aktuelle Position
        self.x = x
        self.y = y
        self.angle = 0 # Das Hindernis steht aufrecht
        self.start() # Sofort nach Erzeugung starten

    def start(self):
        self.aktiv = True
        
    def stopp(self):
        self.aktiv = False

    def kollision(self):
        self.angle = -90 # Das Hindernis ist umgefallen
        self.stopp()

    def update(self):
        if not self.aktiv: return
        self.x -= 2 # Zwei Pixel nach links
        