class Study:
    def __init__(self, name, state, gain=1, intelligence=0, gain_tiredness=1, gain_hunger=1, gain_happiness=1, gain_physical_health=0):
        self.name = name
        self.gain = gain
        self.intelligence = intelligence
        self.state = state
        self.gain_tiredness = gain_tiredness
        self.gain_hunger = gain_hunger
        self.gain_happiness = gain_happiness
        self.gain_physical_health = gain_physical_health

    def get_studies_by_intelligence(intelligence):
        studies = sorted([formes, chiffres, lecture, ecriture, geographie, sciences, maths, histoire, philosophie, psychologie, sociologie, economies, informatique, gameDesign], key=lambda x: x.intelligence)
        return [study for study in studies if study.intelligence <= intelligence]

#Création d'études (valeurs ajustées pour être des points absolus jouables)
    #Bébé
formes = Study("Formes", "Bébé", gain=10, intelligence=0, gain_tiredness=5, gain_hunger=2, gain_happiness=1, gain_physical_health=5)
chiffres = Study("Chiffres", "Bébé", gain=10, intelligence=0, gain_tiredness=5, gain_hunger=2, gain_happiness=1, gain_physical_health=5)
    #Enfant - apprentissages de base
lecture = Study("Lecture", "Enfant", gain=15, intelligence=0, gain_tiredness=10, gain_hunger=5, gain_happiness=2, gain_physical_health=5)
ecriture = Study("Ecriture", "Enfant", gain=15, intelligence=0, gain_tiredness=10, gain_hunger=5, gain_happiness=2, gain_physical_health=5)

geographie = Study("Géographie", "Enfant", gain=18, intelligence=1.50, gain_tiredness=20, gain_hunger=6, gain_happiness=2, gain_physical_health=8)
sciences = Study("Sciences", "Enfant", gain=20, intelligence=1.70, gain_tiredness=20, gain_hunger=6, gain_happiness=2, gain_physical_health=8)
maths = Study("Maths", "Enfant", gain=20, intelligence=1.60, gain_tiredness=20, gain_hunger=6, gain_happiness=2, gain_physical_health=8)
histoire = Study("Histoire", "Enfant", gain=15, intelligence=1.50, gain_tiredness=20, gain_hunger=6, gain_happiness=2, gain_physical_health=8)
    #Adulte - études avancées
philosophie = Study("Philosophie", "Adulte", gain=21, intelligence=3, gain_tiredness=25, gain_hunger=8, gain_happiness=3, gain_physical_health=10)
psychologie = Study("Psychologie", "Adulte", gain=25, intelligence=3, gain_tiredness=25, gain_hunger=10, gain_happiness=3, gain_physical_health=10)
sociologie = Study("Sociologie", "Adulte", gain=25, intelligence=3, gain_tiredness=25, gain_hunger=10, gain_happiness=3, gain_physical_health=10)
economies = Study("Economies", "Adulte", gain=25, intelligence=3, gain_tiredness=25, gain_hunger=10, gain_happiness=4, gain_physical_health=10)
informatique = Study("Informatique", "Adulte", gain=25, intelligence=3.5, gain_tiredness=30, gain_hunger=12, gain_happiness=4, gain_physical_health=10)
gameDesign = Study("Game Design", "Adulte", gain=25, intelligence=3, gain_tiredness=30, gain_hunger=12, gain_happiness=5, gain_physical_health=10)