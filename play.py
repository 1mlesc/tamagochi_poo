class Play:
    def __init__ (self, name, gain=100, intelligence=1):
        self.name = name
        self.gain = gain
        self.intelligence = intelligence

#Création de jouets
    #Ballon :
    #   BAsique
petiteBalle = Play("Petite balle", 20, 0)
ballon = Play("Ballon", 20, 0)
    #   Amélioration
balleTennis = Play("Balle de tennis", 50, 50)
ballonFoot = Play("Ballon de foot", 70, 100)
ballonBasket = Play("Ballon de basket", 90, 150)
ballonRugby = Play("Ballon de rugby", 100, 200)

poupée = Play("Poupée", 30, 50)
voiture = Play("Voiture", 50, 80)
peluche = Play("Peluche", 55, 100)
lego = Play("Lego", 60, 150)
puzzle = Play("Puzzle", 75, 200)
carte = Play("Carte", 90, 250)
console = Play("Console", 100, 500)