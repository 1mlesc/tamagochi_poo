class Food:
    def __init__(self, name, state, goodEffect=None, badEffect=None, money=10, gain=100):
        self.name = name
        self.type = type
        self.gain = gain
        self.money = money
        self.state = state
        self.goodEffect = goodEffect
        self.badEffect = badEffect

    def get_foods_by_state(state):
        if state == "Bébé":
            return [biberon]
        elif state == "Enfant":
            return [confitureFramboise, confitureFraise, confiturePomme, confiturePoire, confiturePeche]
        elif state == "Adulte":
            return [croissant, chocolat, tarte, pomme, poire]
        else:
            return [possionFaim]
        
#Création de nourriture
    #Bébé
biberon = Food("Biberon", "Bébé", gain=75)

    #Enfant
confitureFramboise = Food("Confiture de Framboise", "Enfant", gain=50, goodEffect="Amélioration de l'étude", badEffect="Diminution du jeu")
confitureFraise = Food("Confiture de Fraise", "Enfant", gain=50, goodEffect="Amélioration de l'humeur", badEffect="Diminution de la santé")
confiturePomme = Food("Confiture de Pomme", "Enfant", gain=50, goodEffect="Amélioration du jeu", badEffect="Diminution de l'énergie")
confiturePoire = Food("Confiture de Poire", "Enfant", gain=50, goodEffect="Amélioration de la santé", badEffect="Diminution de l'humeur")
confiturePeche = Food("Confiture de Pêche", "Enfant", gain=50, goodEffect="Amélioration de l'énergie", badEffect="Diminution de l'étude")

    #Adulte
croissant = Food("Croissant", "Adulte", gain=25, goodEffect="Amélioration de l'étude", badEffect="Diminution de la santé")
chocolat = Food("Chocolat", "Adulte", gain=25, goodEffect="Amélioration de l'humeur", badEffect="Diminution de l'énergie")
tarte = Food("Tarte", "Adulte", gain=50, goodEffect="Amélioration du jeu", badEffect="Diminution de l'étude")
bolonise = Food("Bolonièse", "Adulte", gain=50, goodEffect="Amélioration de la santé", badEffect="Diminution de l'humeur")
pomme = Food("Pomme", "Adulte", gain=25, goodEffect="Amélioration de la santé", badEffect="Diminution de l'humeur")
poire = Food("Poire", "Adulte", gain=25, goodEffect="Amélioration de l'énergie", badEffect="Diminution de la santé")

    #Autre
possionFaim = Food("Poisson Faim", gain=100)