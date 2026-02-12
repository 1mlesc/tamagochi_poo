from study import Study
from food import Food
from job import Job
from play import Play
from observer import Observable
#from sport import Sport

class Creature(Observable):
    def __init__(self, name, happiness=50, intelligence=1, tiredness=30, hunger=30, health=100, state="Bébé", money=0, steps=0):
      super().__init__()
      self.name = name
      self.state = state
      self.happiness = happiness
      self.intelligence = intelligence
      self.tiredness = tiredness
      self.hunger = hunger
      self.health = health
      self.physical_health = health
      self.money = money
      self.steps = steps

    #Ajout de l'observateur pour la créature
    def add_observer(self, observer):
      super().add_observer(observer)

    #Fonction pour faire manger la créature
    def eat(self, food: Food):
      gain = food.gain
      self.decrease_hunger(gain)
      self.increase_steps()
      self.increase_happiness(8)
      self.increase_physical_health(5)

      self.increase_tiredness(5)
      self.notify("eat", gain)


    #Fonction pour faire dormir la créature
    def sleep(self):
      self.notify("sleep")
      self.reset_tiredness()
      self.increase_happiness(5)
      self.increase_health(10)
      self.increase_steps()

      self.increase_hunger(25)

      self.notify("sleep")


    #Fonction pour faire étudier la créature
    def study(self, subject: Study):
      gain = subject.gain
      self.increase_intelligence(gain)
      self.increase_steps()

      self.increase_tiredness(20)
      self.increase_hunger(15)
      self.decrease_happiness(5)
      self.decrease_physical_health(2)

      self.notify("study", gain)


    #Fonction pour faire jouer la créature
    def play(self, play: Play):
      self.notify("play")
      gain = play.gain
      self.increase_happiness(gain)
      self.increase_steps()

      self.decrease_intelligence(3)
      self.increase_hunger(10)
      
      self.notify("play")

    #Fonction pour faire faire du sport à la créature
    def sport(self, sport: Sport):
      self.notify("sport")
  
    #Fonction pour faire se laver la créature
    def wash(self):
      # Augmentation de la vie
      self.increase_happiness()
      self.increase_steps()
      self.increase_health(10)
      self.increase_physical_health(10)
      
      # Dégradation de la vie
      self.increase_hunger(10)

      self.notify("wash")

    #Fonction pour faire travailler la créature
    def work(self, job: Job):
      self.increase_money(job.salary)
      self.increase_steps()
      self.increase_intelligence(5)

      self.decrease_health(6)
      self.increase_hunger(15)
      self.decrease_happiness(7)
      self.decrease_physical_health(3)

      self.notify("work", job)

    #Fonction pour baisser l'intelligence en pourcentage
    def decrease_intelligence(self, amount):
      self.intelligence -= self.intelligence * amount / 100
      if self.intelligence < 0:
        self.intelligence = 0

    #Fonction pour augmenter l'intelligence en pourcentage
    def increase_intelligence(self, amount):
      self.intelligence += self.intelligence * amount / 100
      if self.intelligence > 100:
        self.intelligence = 100


    def increase_physical_health(self, amount):
      self.physical_health += amount
      if self.physical_health > 100:
        self.physical_health = 100

    def decrease_physical_health(self, amount):
      self.physical_health -= amount
      if self.physical_health < 0:
        self.physical_health = 0

    #Fonction pour gérer la fatigue
    def increase_tiredness(self, amount):
      self.tiredness += amount
      if self.tiredness > 100:
        self.tiredness = 100
    
    def decrease_tiredness(self, amount):
      self.tiredness -= amount
      if self.tiredness < 0:
        self.tiredness = 0

    def reset_tiredness(self):
      self.tiredness = 0
    
    #Fonction pour augmenter l'argent
    def increase_money(self, amount):
      self.money += amount
      gain = amount / 100
      self.increase_happiness(gain)

    def decrease_money(self, amount):
      self.money -= amount
      self.decrease_happiness(amount)

    #Fonction pour augmenter la faim
    def increase_hunger(self, amount):
      self.hunger += amount
      if self.hunger > 100:
        self.hunger = 100

    #Fonction pour baisser la faim
    def decrease_hunger(self, amount):
      self.hunger -= amount
      if self.hunger < 0:
        self.hunger = 0
    
    #Fonction pour augmenter la santé
    def increase_health(self, amount):
      self.health += amount
      if self.health > 100:
        self.health = 100

    #Fonction pour baisser la santé
    def decrease_health(self, amount):
      self.health -= amount
      if self.health < 0:
        self.health = 0

    #Augmentation des étapes de la vie
    # Lorsque les étapes atteignent 8, la créature évolue
    def increase_steps(self):
      self.steps +=1
      if self.steps == 8:
        self.steps = 0
        self.evolve()

    def increase_happiness(self, amount=5):
      self.happiness += amount
      if self.happiness > 100:
        self.happiness = 100
    
    def decrease_happiness(self, amount=5):
      self.happiness -= amount
      if self.happiness < 0:
        self.happiness = 0

    def evolve(self):
      if self.state == "Bébé":
        self.state = "Enfant"
        self.notify("evolve_kid")
      elif self.state == "Enfant":
        self.state = "Adulte"
        self.notify("evolve_adult")
      elif self.state == "Adulte":
        self.state = "Vieux"
        self.notify("evolve_old")

    def show_status(self):
      print("Nom : " + self.name)
      print("État : " + self.state)
      print("Happiness : " + self.show_happiness())
      print("Intelligence : " + self.show_intelligence())
      print("Fatigue : " + self.show_tiredness())
      print("Faim : " + self.show_hunger())
      print("Santé : " + self.show_health())
      print("Santé physique : " + self.show_physical_health())
      print("Argent : " + self.show_money())
    #Fonction pour montrer l'état de la créature
    def show_happiness(self):
        if self.happiness > 80:
            return "Très heureux : " + str(self.happiness) 
        elif self.happiness > 60:
            return "Heureux : " + str(self.happiness)
        elif self.happiness > 40:
            return "Neutre : " + str(self.happiness) 
        elif self.happiness > 20:
            return "Triste : " + str(self.happiness) 
        else:
            return "Très triste : " + str(self.happiness) 

    #Monter l'intelligence de la créature
    def show_intelligence(self):
        if self.intelligence > 80:
            return "Très intelligent : " + str(self.intelligence) 
        elif self.intelligence > 60:
            return "Intelligent : " + str(self.intelligence) 
        elif self.intelligence > 40:
            return "Neutre : " + str(self.intelligence) 
        elif self.intelligence > 20:
            return "Peu intelligent : " + str(self.intelligence) 
        else:
            return "Très peu intelligent : " + str(self.intelligence) 
    
    #Montrer la fatigue de la créature
    def show_tiredness(self):
        if self.tiredness > 80:
            return "Très fatigué : " + str(self.tiredness) 
        elif self.tiredness > 60:
            return "Fatigué : " + str(self.tiredness) 
        elif self.tiredness > 40:
            return "Neutre : " + str(self.tiredness) 
        elif self.tiredness > 20:
            return "Peu fatigué : " + str(self.tiredness) 
        else:
            return "Très peu fatigué : " + str(self.tiredness)

    #Montrer la faim de la créature
    def show_hunger(self):
        if self.hunger > 80:
            return "Très affamé : " + str(self.hunger) 
        elif self.hunger > 60:
            return "Affamé : " + str(self.hunger) 
        elif self.hunger > 40:
            return "Neutre : " + str(self.hunger) 
        elif self.hunger > 20:
            return "Peu affamé : " + str(self.hunger) 
        else:
            return "Très peu affamé : " + str(self.hunger) 
    
    #Montrer la vie de la créature
    def show_health(self):
        if self.health > 80:
            return "Très en bonne santé : " + str(self.health) 
        elif self.health > 60:
            return "En bonne santé : " + str(self.health) 
        elif self.health > 40:
            return "Neutre : " + str(self.health) 
        elif self.health > 20:
            return "En mauvaise santé : " + str(self.health) 
        else:
            return "Très en mauvaise santé : " + str(self.health)
        
    #Montrer la vie physique de la créature
    def show_physical_health(self):
        if self.physical_health > 80:
            return "Très en bonne santé physique : " + str(self.physical_health) 
        elif self.physical_health > 60:
            return "En bonne santé physique : " + str(self.physical_health) 
        elif self.physical_health > 40:
            return "Neutre : " + str(self.physical_health) 
        elif self.physical_health > 20:
            return "En mauvaise santé physique : " + str(self.physical_health) 
        else:
            return "Très en mauvaise santé physique : " + str(self.physical_health)
    
    #Montrer l'argent de la créature
    def show_money(self):
        if self.money > 80:
            return "Très riche : " + str(self.money) 
        elif self.money > 60:
            return "Riche : " + str(self.money) 
        elif self.money > 40:
            return "Neutre : " + str(self.money) 
        elif self.money > 20:
            return "Pauvre : " + str(self.money) 
        else:
            return "Très pauvre : " + str(self.money)

    def is_alive(self):
      return self.health > 0
    
    def die(self):
      if not self.is_alive(): 
          self.notify("die")

