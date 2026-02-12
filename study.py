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
formes = Study("Formes", "Bébé", 1, 0)
chiffres = Study("Chiffres", "Bébé", 1, 0)
    #Enfant
lecture = Study("Lecture", "Enfant", 1.5, 0)
ecriture = Study("Ecriture", "Enfant", 1.5, 0)

geographie = Study("Géographie", "Enfant", 2, 5)
sciences = Study("Sciences", "Enfant", 2, 5)
maths = Study("Maths", "Enfant", 2, 5)
histoire = Study("Histoire", "Enfant", 2, 5)
    #Adulte
philosophie = Study("Philosophie", "Adulte", 3, 10)
psychologie = Study("Psychologie", "Adulte", 3.5, 30)
sociologie = Study("Sociologie", "Adulte", 4, 35)
economies = Study("Economies", "Adulte", 4.5, 40)
informatique = Study("Informatique", "Adulte", 5, 50)
gameDesign = Study("Game Design", "Adulte", 5.5, 70)