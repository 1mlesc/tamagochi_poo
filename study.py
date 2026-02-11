class Study:
    def __init__(self, name, state, gain=100, intelligence=1):
        self.name = name
        self.gain = gain
        self.intelligence = intelligence
        self.state = state

    def get_studies_by_state(state):
        if state == "Bébé":
            return [formes, chiffres]
        elif state == "Enfant":
            return [lecture, ecriture]
        elif state == "Adulte":
            return [philosophie, psychologie, sociologie, economies, informatique, gameDesign]
        else:
            return []

#Création d'études
    #Bébé
formes = Study("Formes", "Bébé", 2, 0)
chiffres = Study("Chiffres", "Bébé", 2, 0)
    #Enfant
lecture = Study("Lecture", "Enfant", 5, 0)
ecriture = Study("Ecriture", "Enfant", 5, 0)

geographie = Study("Géographie", "Enfant", 8, 10)
sciences = Study("Sciences", "Enfant", 8, 10)
maths = Study("Maths", "Enfant", 8, 10)
histoire = Study("Histoire", "Enfant", 8, 10)
    #Adulte
philosophie = Study("Philosophie", "Adulte", 10, 15)
psychologie = Study("Psychologie", "Adulte", 10, 15)
sociologie = Study("Sociologie", "Adulte", 12, 30)
economies = Study("Economies", "Adulte", 12, 30)
informatique = Study("Informatique", "Adulte", 12, 30)
gameDesign = Study("Game Design", "Adulte", 15, 50)