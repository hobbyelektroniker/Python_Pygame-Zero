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

class Spieler(Actor):
    def __init__(self, x, y):
        super().__init__('run__000')
        self.aktiv = False
        # Die Grundposition speichern
        self.baseX = x
        self.baseY = y
        # Die aktuelle Position
        self.x = x
        self.y = y
        # Laden der Bilder für die Animation
        self.images = []
        for i in range(10):
            self.images.append("run__{:03d}".format(i))
            
    def start(self):
        # Aufrecht stehender Spieler an der Grundposition
        self.x = self.baseX
        self.y = self.baseY
        self.angle = 0
        self.aktiv = True
        
    def stopp(self):
        self.aktiv = False
        
    def sprung(self):
        if self.y >= self.baseY:
            # nur wenn der Spieler am Boden ist, erfolgt ein grosser Sprung
            self.y = self.baseY - 350
        else:
            # sonst wird der Fall nur etwas abgebremst
            self.y -= 19

    def kollision(self):
        self.angle = -90    # Spierler fällt um
        self.y = self.baseY # er liegt am Boden
        self.stopp()

    def update(self):
        if not self.aktiv: return
        if self.y < self.baseY:
            # Wenn der Spieler nicht am Boden ist, fällt er (Schwerkraft).
            self.y += 20
        self.next_image() # Das nächste Bild der Animation wird angezeigt
        