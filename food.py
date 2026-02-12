class Food:
    def __init__(self, name, state, goodEffect=None, badEffect=None, money=10, gain=100, gain_happiness=1, gain_physical_health=1, gain_health=1, gain_tiredness=1):
        self.name = name
        self.type = type
        self.gain = gain
        self.money = money
        self.state = state
        self.goodEffect = goodEffect
        self.badEffect = badEffect
        self.gain_happiness = gain_happiness
        self.gain_physical_health = gain_physical_health
        self.gain_health = gain_health
        self.gain_tiredness = gain_tiredness

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
biberon = Food("Biberon", "Bébé", gain=75, gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)

    #Enfant
confitureFramboise = Food("Confiture de Framboise", "Enfant", gain=50, goodEffect="Amélioration de l'étude", badEffect="Diminution du jeu",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
confitureFraise = Food("Confiture de Fraise", "Enfant", gain=50, goodEffect="Amélioration de l'humeur", badEffect="Diminution de la santé",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
confiturePomme = Food("Confiture de Pomme", "Enfant", gain=50, goodEffect="Amélioration du jeu", badEffect="Diminution de l'énergie",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
confiturePoire = Food("Confiture de Poire", "Enfant", gain=50, goodEffect="Amélioration de la santé", badEffect="Diminution de l'humeur",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
confiturePeche = Food("Confiture de Pêche", "Enfant", gain=50, goodEffect="Amélioration de l'énergie", badEffect="Diminution de l'étude",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)

    #Adulte
croissant = Food("Croissant", "Adulte", gain=25, goodEffect="Amélioration de l'étude", badEffect="Diminution de la santé",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
chocolat = Food("Chocolat", "Adulte", gain=25, goodEffect="Amélioration de l'humeur", badEffect="Diminution de l'énergie",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
tarte = Food("Tarte", "Adulte", gain=50, goodEffect="Amélioration du jeu", badEffect="Diminution de l'étude",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
bolonise = Food("Bolonièse", "Adulte", gain=50, goodEffect="Amélioration de la santé", badEffect="Diminution de l'humeur",  gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
pomme = Food("Pomme", "Adulte", gain=25, goodEffect="Amélioration de la santé", badEffect="Diminution de l'humeur",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)
poire = Food("Poire", "Adulte", gain=25, goodEffect="Amélioration de l'énergie", badEffect="Diminution de la santé",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)

    #Autre
possionFaim = Food("Poisson Faim","Vieux", gain=100,goodEffect="Amélioration de la santé", badEffect="Diminution de l'humeur",gain_happiness=5, gain_physical_health=5, gain_health=5, gain_tiredness=5)