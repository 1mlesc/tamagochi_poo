from study import Study
from food import Food
from work import Work
from play import Play
from sport import Sport

class Creature:
    def __init__(self, name, happiness=50, intelligence=1, tiredness=30, hunger=30, health=100, state="Bébé", money=0, steps=0):
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


    #Fonction pour faire manger la créature
    def eat(self, food: Food):
      gain = food.gain
      self.hunger + self.hunger + gain
      self.increase_steps()
      self.increase_happiness()
      return self.hunger


    #Fonction pour faire dormir la créature
    def sleep(self):
      pass


    #Fonction pour faire étudier la créature
    def study(self, subject: Study):
      gain = subject.gain
      self.intelligence += self.intelligence * gain / 100
      self.increase_steps()
      return self.intelligence

    #Fonction pour faire jouer la créature
    def play(self, play: Play):
      pass

    #Fonction pour faire faire du sport à la créature
    def sport(self, sport: Sport):
      pass
  
    #Fonction pour faire se laver la créature
    def wash(self):
      # Augmentation de la vie
      self.increase_happiness()
      self.increase_steps()
      self.increase_health(20)
      self.increase_physical_health(20)
      
      # Dégradation de la vie
      self.increase_hunger(10)

    #Fonction pour faire travailler la créature, plus la créature est intelligente, plus elle gagne de l'argent et du bonheur
    def work(self, work: Work):
      pass

    #Fonction pour dormir
    def sleep(self):
       self.tiredness = 0
       self.increase_happiness()
       self.increase_health(10)
       self.increase_steps()

       self.increase_hunger(20)

    #Fonction pour augmenter la faim
    def increase_hunger(self, amount):
      self.hunger += amount
      if self.hunger > 100:
        self.hunger = 100
        self.decrease_health(10)
    
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

    def increase_happiness(self):
      self.happiness += 5
      if self.happiness > 100:
        self.happiness = 100
    
    def decrease_happiness(self):
      self.happiness -= 5
      if self.happiness < 0:
        self.happiness = 0

    def evolve(self):
      if self.state == "Bébé":
        self.state = "Enfant"
      elif self.state == "Enfant":
        self.state = "Adulte"
      elif self.state == "Adulte":
        self.state = "Vieux"

    #Fonction pour montrer l'état de la créature
    def show_happiness(self):
        if self.happiness > 80:
            return "Très heureux : " + self.happiness 
        elif self.happiness > 60:
            return "Heureux : " + self.happiness 
        elif self.happiness > 40:
            return "Neutre : " + self.happiness 
        elif self.happiness > 20:
            return "Triste : " + self.happiness 
        else:
            return "Très triste : " + self.happiness 

    def is_alive(self):
      return self.health > 0

