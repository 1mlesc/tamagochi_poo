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
formes = Study("Formes", "Bébé", 20, 0)
chiffres = Study("Chiffres", "Bébé", 20, 0)
    #Enfant
lecture = Study("Lecture", "Enfant", 30, 0)
ecriture = Study("Ecriture", "Enfant", 30, 0)

geographie = Study("Géographie", "Enfant", 40, 50)
sciences = Study("Sciences", "Enfant", 40, 50)
maths = Study("Maths", "Enfant", 40, 50)
histoire = Study("Histoire", "Enfant", 40, 50)
    #Adulte
philosophie = Study("Philosophie", "Adulte", 40, 50)
psychologie = Study("Psychologie", "Adulte", 40, 50)
sociologie = Study("Sociologie", "Adulte", 70, 100)
economies = Study("Economies", "Adulte", 80, 120)
informatique = Study("Informatique", "Adulte", 90, 140)
gameDesign = Study("Game Design", "Adulte", 100, 150)