class Study:
    def __init__(self, name, state, gain=100, intelligence=1, gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1):
        self.name = name
        self.gain = gain
        self.intelligence = intelligence
        self.state = state
        self.gain_tiredness = gain_tiredness
        self.gain_hunger = gain_hunger
        self.gain_happiness = gain_happiness
        self.gain_physical_health = gain_physical_health

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
formes = Study("Formes", "Bébé", 1, 0,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
chiffres = Study("Chiffres", "Bébé", 1, 0,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
    #Enfant
lecture = Study("Lecture", "Enfant", 1.5, 0,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
ecriture = Study("Ecriture", "Enfant", 1.5, 0,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)

geographie = Study("Géographie", "Enfant", 2, 5,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
sciences = Study("Sciences", "Enfant", 2, 5,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
maths = Study("Maths", "Enfant", 2, 5,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
histoire = Study("Histoire", "Enfant", 2, 5,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
    #Adulte
philosophie = Study("Philosophie", "Adulte", 3, 10,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
psychologie = Study("Psychologie", "Adulte", 3.5, 30,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
sociologie = Study("Sociologie", "Adulte", 4, 35,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
economies = Study("Economies", "Adulte", 4.5, 40,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
informatique = Study("Informatique", "Adulte", 5, 50,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)
gameDesign = Study("Game Design", "Adulte", 5.5, 70,gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=1)