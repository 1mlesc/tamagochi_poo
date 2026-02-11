class Food:
    def __init__(self, name, type, effect=None, gain=100):
        self.name = name
        self.type = type
        self.gain = gain
        self.effect = effect


#Création de nourriture
    #Bébé
biberon = Food("Biberon", 1, gain=75, effect="x")

    #Enfant
confitureFramboise = Food("Confiture de Framboise", 2, gain=50, effect="x")
confitureFraise = Food("Confiture de Fraise", 2, gain=50, effect="x")
confiturePomme = Food("Confiture de Pomme", 2, gain=50, effect="x")
confiturePoire = Food("Confiture de Poire", 2, gain=50, effect="x")
confiturePeche = Food("Confiture de Pêche", 2, gain=50, effect="x")

    #Adulte
croissant = Food("Croissant", 3, gain=50, effect="x")
chocolat = Food("Chocolat", 3, gain=50, effect="x")
tarte = Food("Tarte", 3, gain=50, effect="x")
pomme = Food("Pomme", 3, gain=50, effect="x")
poire = Food("Poire", 3, gain=50, effect="x")

    #Autre
possionFaim = Food("Poisson Faim", 3, gain=50, effect="x")

# favorite pour créature
# nombre de récupération de nourriture
# if nourriture favorite, +5 au gain de nourriture
# certaine nourriture boost et d'autre réduise tel ou tel effet