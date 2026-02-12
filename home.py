class Home:
    def __init__(self, name, rent):
        self.name = name
        self.rent = rent

#Création de différentes maisons
parents_home = Home("Maison des parents", 0)
apartment = Home("Appartement", 200)
house = Home("Maison", 500)
villa = Home("Villa", 1500)