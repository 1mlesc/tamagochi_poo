class Job :
    def __init__(self, name, salary, intelligence, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=0, gain_physical_health=0, gain_health=0):
        self.name = name
        self.salary = salary
        self.intelligence = intelligence
        self.gain_happiness = gain_happiness
        self.gain_hunger = gain_hunger
        self.gain_tiredness = gain_tiredness 
        self.gain_intelligence = gain_intelligence
        self.gain_physical_health = gain_physical_health
        self.gain_health = gain_health

    #Retourner les jobs disponibles en fonction de l'intelligence de la créature
    def get_jobs_by_state(intelligence):
        jobs = sorted([chomage, ouvrier, fastFood, vendeur, secretaire, freelance, enseignant, dentiste, ingenieur, veterinaire, medecin, pilote, avocat, chef, juge, dieu], key=lambda x: x.intelligence)
        return [job for job in jobs if job.intelligence <= intelligence]

#Création de jobs
chomage = Job("Chômage", 10, 0, gain_happiness=10, gain_hunger=5, gain_tiredness=5, gain_intelligence=0, gain_physical_health=5, gain_health=5)
ouvrier = Job("Ouvrier", 100, 2, gain_happiness=6, gain_hunger=8, gain_tiredness=70, gain_intelligence=10, gain_physical_health=6, gain_health=6)
fastFood = Job("Fast Food", 200, 2.10, gain_happiness=5, gain_hunger=10, gain_tiredness=70, gain_intelligence=10, gain_physical_health=8, gain_health=8)
vendeur = Job("Vendeur", 500, 2.4, gain_happiness=4, gain_hunger=12, gain_tiredness=50, gain_intelligence=15, gain_physical_health=8, gain_health=8)
secretaire = Job("Secrétaire", 1000, 3, gain_happiness=3, gain_hunger=14, gain_tiredness=50, gain_intelligence=20, gain_physical_health=10, gain_health=10)
freelance = Job("Freelance", 2000, 4, gain_happiness=3, gain_hunger=15, gain_tiredness=30, gain_intelligence=40, gain_physical_health=10, gain_health=10)
enseignant = Job("Enseignant", 2000, 4, gain_happiness=2, gain_hunger=10, gain_tiredness=50, gain_intelligence=40, gain_physical_health=5, gain_health=5)
dentiste = Job("Dentiste", 3000, 5, gain_happiness=2, gain_hunger=18, gain_tiredness=50, gain_intelligence=30, gain_physical_health=10, gain_health=10)
ingenieur = Job("Ingénieur", 5000, 6, gain_happiness=2, gain_hunger=20, gain_tiredness=50, gain_intelligence=35, gain_physical_health=12, gain_health=12)
veterinaire = Job("Vétérinaire", 15000, 8, gain_happiness=1, gain_hunger=22, gain_tiredness=50, gain_intelligence=35, gain_physical_health=12, gain_health=12)
medecin = Job("Médecin", 10000, 10, gain_happiness=1, gain_hunger=24, gain_tiredness=55, gain_intelligence=45, gain_physical_health=15, gain_health=15)
pilote = Job("Pilote", 20000, 15, gain_happiness=1, gain_hunger=26, gain_tiredness=60, gain_intelligence=25, gain_physical_health=15, gain_health=15)
avocat = Job("Avocat", 50000, 22, gain_happiness=3, gain_hunger=32, gain_tiredness=60, gain_intelligence=50, gain_physical_health=18, gain_health=18)
chef = Job("Chef", 100000, 29, gain_happiness=3, gain_hunger=34, gain_tiredness=90, gain_intelligence=19, gain_physical_health=18, gain_health=18)
juge = Job("Juge", 500000, 43, gain_happiness=2, gain_hunger=36, gain_tiredness=50, gain_intelligence=60, gain_physical_health=20, gain_health=20)
dieu = Job("Dieu", 1000000000, 60, gain_happiness=0, gain_hunger=40, gain_tiredness=0, gain_intelligence=100, gain_physical_health=25, gain_health=25)