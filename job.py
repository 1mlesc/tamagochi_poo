class Job :
    def __init__(self, name, salary, intelligence):
        self.name = name
        self.salary = salary
        self.intelligence = intelligence

    #Retourner les jobs disponibles en fonction de l'intelligence de la créature
    def get_jobs_by_state(intelligence):
        jobs = sorted([chomage, ouvrier, fastFood, vendeur, secretaire, freelance, enseignant, dentiste, ingenieur, veterinaire, medecin, pilote, boxeur, youtuber, avocat, chef, juge, dieu], key=lambda x: x.intelligence)
        return [job for job in jobs if job.intelligence <= intelligence]

#Création de jobs
chomage = Job("Chômage", 10, 0)
ouvrier = Job("Ouvrier", 100, 5)
fastFood = Job("Fast Food", 200, 10)
vendeur = Job("Vendeur", 500, 15)
secretaire = Job("Secrétaire", 1000, 20)
freelance = Job("Freelance", 2000, 25)
enseignant = Job("Enseignant", 2000, 30)
dentiste = Job("Dentiste", 3000, 35)
ingenieur = Job("Ingénieur", 5000, 40)
veterinaire = Job("Vétérinaire", 15000, 45)
medecin = Job("Médecin", 10000, 50)
pilote = Job("Pilote", 20000, 55)
boxeur = Job("Boxeur", 50000, 60)
youtuber = Job("Youtuber", 100000, 65)
avocat = Job("Avocat", 50000, 70)
chef = Job("Chef", 100000, 75)
juge = Job("Juge", 500000, 80)
dieu = Job("Dieu", 1000000000, 90)