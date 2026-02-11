class Play:
    def __init__ (self, name, type, level=1):
        self.name = name
        self.type = type
        self.level = level

#Création de jouets
    #Ballon :
    #   Niveau 1
petiteBalle = Play("Petite balle", 1)
ballon = Play("Ballon", 1)
    #   Niveau 2
balleTennis = Play("Balle de tennis", 2)
ballonFoot = Play("Ballon de foot", 2)
    #   Niveau 3
ballonBasket = Play("Ballon de basket", 3)
ballonRugby = Play("Ballon de rugby", 3)

    #Autres :
    #   Niveau 2
poupée = Play("Poupée", 2)
    #   Niveau 3
voiture = Play("Voiture", 3)
peluche = Play("Peluche", 3)
    #   Niveau 4
lego = Play("Lego", 4)
puzzle = Play("Puzzle", 4)
    #   Niveau 5
console = Play("Console", 5)
carte = Play("Carte", 5)