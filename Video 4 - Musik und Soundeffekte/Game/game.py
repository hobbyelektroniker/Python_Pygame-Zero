'''
  Gameprogrammierung mit Python und Pygame Zero
  Version 1.00, 25.09.2021
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

# Ein einfaches Spiel mit 3 Elementen
# Das Spielfeld: Hintergrund mit Punkteanzeige
# Der Spieler: animierte Figur, die springen kann
# Die Hindernisse: tauchen unregelmässig auf und müssen übersprungen werden
# Ziel: Möglichst viele Hindernisse nicht berühren

'''
Video 4
Musik und Soundeffekte
'''

import pgzrun
from spieler import Spieler
from hindernis import Hindernis
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Jump and Run"
HIMMEL = 400

class Spiel:
    def __init__(self):
        self.aktiv = False     # Spiel nicht aktiv 
        self.finished = False  # Kein beendetes Spiel
        self.punkte = 0        # Der Punktestand ist 0
        self.spieler = Spieler(100,HIMMEL) # Der Spieler wird erzeugt
        self.hindernisse = []  # Leere Liste für die Hindernisse
        self.hinderniszeit = 0 # Zähler für die Ereugung des nächsten Hindenisses
        random.seed()          # Zufallsgenerator initialisieren

    def start(self):
        self.aktiv = True        # Das Spiel ist aktiv
        self.finished = False    # Das Spiel ist noch nicht beendet
        self.punkte = 0          # Punktestand 0
        self.hindernisse.clear() # Alle Hindernisse entfernen
        self.spieler.start()     # Der Spieler muss hier gestartet werden
        music.play("venus.wav")  # Die Musik wird gestartet
        
    def stopp(self):
        self.aktiv = False       # Das Spiel ist nicht mehr aktiv
        self.finished = True     # Das Spiel ist beendet
        self.spieler.stopp()     # Ein Spielstopp soll auch den Spieler stoppen
        music.stop()             # Die Musik wird gestoppt

    def zeichne_spielfeld(self):
        farbe_himmel = (163, 232, 254) # blau
        screen.draw.filled_rect(Rect(0, 0, WIDTH, HIMMEL), farbe_himmel)
        farbe_boden = (88, 242, 152) # grün
        screen.draw.filled_rect(Rect(0, HIMMEL, WIDTH, WIDTH - HIMMEL), farbe_boden)
        farbe_schrift = (255, 255, 255) # weiss
        screen.draw.text(str(self.punkte), (WIDTH - 80, 10), fontsize=60, color=farbe_schrift)
        if self.finished:
            screen.draw.text("GAME OVER", (20, 20), fontsize=80, color=(255, 0, 0))
            screen.draw.text("Neues Spiel mit S", (20, 80), fontsize=60, color=(255, 255, 0))            
        elif not self.aktiv:
            screen.draw.text("Spiel starten mit S", (20, 20), fontsize=60, color=(255, 255, 0))
        
    def zeichne_spieler(self):
        self.spieler.draw()

    def zeichne_hindernisse(self):
        for hindernis in self.hindernisse:
            hindernis.draw()        

    def draw(self):
        self.zeichne_spielfeld()
        self.zeichne_spieler()
        self.zeichne_hindernisse()

    def update(self):
        # Start-Taste nur abfragen, wenn das Spiel nicht aktiv ist
        if not self.aktiv and keyboard.s:
            # neues Spiel starten
            self.start()
 
        # Wenn das Spiel nicht aktiv ist, hier abbrechen
        if not self.aktiv: return
        
        if keyboard.up:
            # Wenn die UP-Taste gedrückt wird, soll der Spieler springen
            self.spieler.sprung()
            
        # Die Update-Methode jeder Figur muss aufgerufen werden
        self.spieler.update()
        
        # Ein neues Hindernis wird erzeugt, wenn die Hinderniszeit abgelaufen ist
        self.hinderniszeit -= 1
        if self.hinderniszeit <= 0:
            hindernis = Hindernis(WIDTH-100, HIMMEL) # Hindernis erzeugen
            self.hindernisse.append(hindernis) # Der Liste hinzufügen
            self.hinderniszeit = random.randint(50, 300) # Neue Hindeniszeit festlegen
            
        for hindernis in self.hindernisse:
            # Auf Kollision testen
            if hindernis.colliderect(self.spieler):
                hindernis.kollision()
                self.spieler.kollision()
                self.stopp() # Hier wird auch die Hintergrundmusik gestoppt
                sounds.gameover.play() # Gameover - Sound abspielen
            # Auf linken Rand testen    
            if hindernis.x < 0:
                self.hindernisse.remove(hindernis)
                self.punkte += 1
                
            hindernis.update()
        

spiel = Spiel()

def update():
    spiel.update()
    
def draw():
    spiel.draw()

pgzrun.go()


