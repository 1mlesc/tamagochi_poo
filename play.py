class Play:
    def __init__ (self, name, gain=100, intelligence=1):
        self.name = name
        self.gain = gain
        self.intelligence = intelligence

#Création de jouets
    #Ballon :
    #   BAsique
petiteBalle = Play("Petite balle", 5, 0)
ballon = Play("Ballon", 5, 0)
    #   Amélioration
balleTennis = Play("Balle de tennis", 10, 5)
ballonFoot = Play("Ballon de foot", 10, 5)
ballonBasket = Play("Ballon de basket", 15, 8)
ballonRugby = Play("Ballon de rugby", 20, 10)

poupée = Play("Poupée", 10, 5)
voiture = Play("Voiture", 10, 5)
peluche = Play("Peluche", 15, 8)
lego = Play("Lego", 15, 8)
puzzle = Play("Puzzle", 25, 10)
carte = Play("Carte", 35, 10)
console = Play("Console", 35, 10)