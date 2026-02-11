class Study:
    def __init__(self, name, level=1, gain=100):
        self.name = name
        self.level = level
        self.gain = gain

    def get_studies_by_state(state):
        if state == "Bébé":
            return [formes, chiffres]
        elif state == "Enfant":
            return [lecture, ecriture]
        elif state == "Adulte":
            return [philosophie, psychologie, sociologie, economies, informatique]
        else:
            return []

#Création
    #Bébé
    #   Niveau 1
formes = Study("Formes", 1, 20)
chiffres = Study("Chiffres", 1, 20)
    #Enfant
    #   Niveau 2
lecture = Study("Lecture", 2, 20)
ecriture = Study("Ecriture", 2, 20)
    #   Niveau 3
geographie = Study("Géographie", 3, 30)
sciences = Study("Sciences", 3, 30)
maths = Study("Maths", 3, 30)
histoire = Study("Histoire", 3, 30)
    #Adulte
    #   Niveau 4
philosophie = Study("Philosophie", 4, 40)
psychologie = Study("Psychologie", 4, 40)
sociologie = Study("Sociologie", 4, 40)
economies = Study("Economies", 4, 40)
informatique = Study("Informatique", 4, 40)
