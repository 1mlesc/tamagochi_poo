class Job :
    def __init__(self, name, salary, intelligence):
        self.name = name
        self.salary = salary
        self.intelligence = intelligence

#Création de jobs
    # 0 =<
chomage = Job("Chômage", 100, 0)
ouvrier = Job("Ouvrier", 500, 100)
    # 100 <
fastFood = Job("Fast Food", 800, 200)
vendeur = Job("Vendeur", 1000, 350)
secretaire = Job("Secrétaire", 1200, 400)
freelance = Job("Freelance", 1400, 500)
    # 500 <
enseignant = Job("Enseignant", 1500, 600)
dentiste = Job("Dentiste", 1800, 750)
ingenieur = Job("Ingénieur", 2000, 800)
veterinaire = Job("Vétérinaire", 2500, 950)
    # 1000 <
medecin = Job("Médecin", 3000, 1100)
pilote = Job("Pilote", 3500, 1200)
boxeur = Job("Boxeur", 4000, 1500)
youtuber = Job("Youtuber", 4500, 2000)
avocat = Job("Avocat", 5000, 5000)
    # 5000 <
chef = Job("Chef", 10000, 10000)
juge = Job("Juge", 15000, 15000)
    #1000000000000 <
dieu = Job("Dieu", 1000000000000, 1000000000000)