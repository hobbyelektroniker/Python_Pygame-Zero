import pgzrun
# Beispiel: from figur import Figur

# Das Spielfeld
WIDTH=800
HEIGHT=600
TITLE = "Ein Spiel"

class Spiel:
    def __init__(self):
        self.aktiv = False
        # Figuren erzeugen
        # Beispiel: self.figur = Figur(10,20)

    def start(self):
        self.aktiv = True
        
    def stopp(self):
        self.aktiv = False

    def zeichne_spielfeld(self):
        pass
        # Beispiel: farbe = (163, 232, 254)
        # Beispiel: screen.draw.filled_rect(Rect(0, 0, WIDTH, HEIGHT), farbe)

    def zeichne_figur(self):
        pass
        # Beispiel: self.figur.draw()

    def draw(self):
        self.zeichne_spielfeld()
        self.zeichne_figur()

    def update(self):
        # Start-Taste nur abfragen, wenn das Spiel nicht aktiv ist
        if not self.aktiv and keyboard.s:
            # neues Spiel starten
            self.start()
 
        # Wenn das Spiel nicht aktiv ist, hier abbrechen
        if not self.aktiv: return

spiel = Spiel()

def update():
    spiel.update()
    
def draw():
    spiel.draw()

pgzrun.go()
