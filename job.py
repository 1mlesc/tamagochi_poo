class Job :
    def __init__(self, name, salary, intelligence):
        self.name = name
        self.salary = salary
        self.intelligence = intelligence

#Création de jobs
chomage = Job("Chômage", 100, 0)
ouvrier = Job("Ouvrier", 1000, 50)
fastFood = Job("Fast Food", 2000, 100)
vendeur = Job("Vendeur", 5000, 150)
secretaire = Job("Secrétaire", 10000, 200)
freelance = Job("Freelance", 20000, 250)
enseignant = Job("Enseignant", 20000, 300)
dentiste = Job("Dentiste", 100000, 400)
ingenieur = Job("Ingénieur", 50000, 500)
veterinaire = Job("Vétérinaire", 150000, 800)
medecin = Job("Médecin", 100000, 1000)
pilote = Job("Pilote", 200000, 1200)
boxeur = Job("Boxeur", 500000, 1500)
youtuber = Job("Youtuber", 1000000, 2000)
avocat = Job("Avocat", 500000, 5000)
chef = Job("Chef", 1000000, 10000)
juge = Job("Juge", 5000000, 15000)
dieu = Job("Dieu", 1000000000000, 1000000000000)