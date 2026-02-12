class Job :
    def __init__(self, name, salary, intelligence, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1, gain_physical_health=1, gain_health=1):
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
        jobs = sorted([chomage, ouvrier, fastFood, vendeur, secretaire, freelance, enseignant, dentiste, ingenieur, veterinaire, medecin, pilote, boxeur, youtuber, avocat, chef, juge, dieu], key=lambda x: x.intelligence)
        return [job for job in jobs if job.intelligence <= intelligence]

#Création de jobs
chomage = Job("Chômage", 10, 0,gain_happiness=-5, gain_hunger=5, gain_tiredness=5, gain_intelligence=0, gain_physical_health=-5, gain_health=-5)
ouvrier = Job("Ouvrier", 100, 5,gain_happiness=-2, gain_hunger=10, gain_tiredness=10, gain_intelligence=0, gain_physical_health=-5, gain_health=-5)
fastFood = Job("Fast Food", 200, 10,gain_happiness=-1, gain_hunger=15, gain_tiredness=15, gain_intelligence=0, gain_physical_health=-10, gain_health=-10)
vendeur = Job("Vendeur", 500, 15,gain_happiness=0, gain_hunger=20, gain_tiredness=20, gain_intelligence=0, gain_physical_health=-10, gain_health=-10)
secretaire = Job("Secrétaire", 1000, 20,gain_happiness=1, gain_hunger=25, gain_tiredness=25, gain_intelligence=0, gain_physical_health=-15, gain_health=-15)
freelance = Job("Freelance", 2000, 25,gain_happiness=2, gain_hunger=30, gain_tiredness=30, gain_intelligence=0, gain_physical_health=-15, gain_health=-15)
enseignant = Job("Enseignant", 2000, 30,gain_happiness=3, gain_hunger=35, gain_tiredness=35, gain_intelligence=0, gain_physical_health=-20, gain_health=-20)
dentiste = Job("Dentiste", 3000, 35,gain_happiness=4, gain_hunger=40, gain_tiredness=40, gain_intelligence=0, gain_physical_health=-20, gain_health=-20)
ingenieur = Job("Ingénieur", 5000, 40,gain_happiness=5, gain_hunger=45, gain_tiredness=45, gain_intelligence=0, gain_physical_health=-25, gain_health=-25)
veterinaire = Job("Vétérinaire", 15000, 45,gain_happiness=6, gain_hunger=50, gain_tiredness=50, gain_intelligence=0, gain_physical_health=-25, gain_health=-25)
medecin = Job("Médecin", 10000, 50,gain_happiness=7, gain_hunger=55, gain_tiredness=55, gain_intelligence=0, gain_physical_health=-30, gain_health=-30)
pilote = Job("Pilote", 20000, 55,gain_happiness=8, gain_hunger=60, gain_tiredness=60, gain_intelligence=0, gain_physical_health=-30, gain_health=-30)
boxeur = Job("Boxeur", 50000, 60,gain_happiness=9, gain_hunger=65, gain_tiredness=65, gain_intelligence=0, gain_physical_health=-35, gain_health=-35)
youtuber = Job("Youtuber", 100000, 65,gain_happiness=10, gain_hunger=70, gain_tiredness=70, gain_intelligence=0, gain_physical_health=-35, gain_health=-35)
avocat = Job("Avocat", 50000, 70,gain_happiness=11, gain_hunger=75, gain_tiredness=75, gain_intelligence=0, gain_physical_health=-40, gain_health=-40)
chef = Job("Chef", 100000, 75,gain_happiness=12, gain_hunger=80, gain_tiredness=80, gain_intelligence=0, gain_physical_health=-40, gain_health=-40)
juge = Job("Juge", 500000, 80,gain_happiness=13, gain_hunger=85, gain_tiredness=85, gain_intelligence=0, gain_physical_health=-45, gain_health=-45)
dieu = Job("Dieu", 1000000000, 95,gain_happiness=14, gain_hunger=90, gain_tiredness=90, gain_intelligence=0, gain_physical_health=-50, gain_health=-50)