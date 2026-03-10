from study import Study
from food import Food
from job import Job
from play import Play
from observer import Observable
from sport import Sport

class Creature(Observable):
    def __init__(self, name, happiness=50, intelligence=1, tiredness=30, hunger=30, health=60, state="Bébé", money=0, physical_health=10, steps=0):
      super().__init__()
      self.name = name
      self.state = state
      #Attributs encaspulés
      self._happiness = happiness
      self._intelligence = intelligence
      self._tiredness = tiredness
      self._hunger = hunger
      self._health = health
      self._physical_health = physical_health
      self._money = money
      self._steps = steps

    #Ajout de l'observateur pour la créature
    def add_observer(self, observer):
      super().add_observer(observer)

    #Fonction pour faire manger la créature
    def eat(self, food: Food):
      self.decrease_hunger(food.gain)
      self.increase_steps()
      self.increase_happiness(food.gain_happiness)
      self.increase_health(food.gain_health)
      self.increase_physical_health(food.gain_physical_health)

      self.increase_tiredness(food.gain_tiredness)
      self.notify("eat", food.gain)


    #Fonction pour faire dormir la créature
    def sleep(self):
      self.reset_tiredness()
      self.increase_happiness(5)
      self.increase_health(10)
      self.increase_steps()

      self.increase_hunger(25)


    #Fonction pour faire étudier la créature
    def study(self, study: Study):
      self.increase_intelligence(study.gain)
      self.increase_steps()

      self.increase_tiredness(study.gain_tiredness)
      self.increase_hunger(study.gain_hunger)
      self.decrease_happiness(study.gain_happiness)
      self.decrease_physical_health(study.gain_physical_health)

      self.notify("study", study.gain)


    #Fonction pour faire jouer la créature
    def play(self, play: Play):
      self.increase_happiness(play.gain_happiness)
      self.increase_steps()

      self.decrease_intelligence(play.gain_intelligence)
      self.increase_hunger(play.gain_hunger)
      self.increase_tiredness(play.gain_tiredness)
      self.notify("play")

    #Fonction pour faire faire du sport à la créature
    def sport(self, sport: Sport):
      self.increase_physical_health(sport.gain_physical_health)
      self.increase_steps()
      self.increase_happiness(sport.gain_happiness)
      
      self.increase_hunger(sport.gain_hunger)
      self.increase_tiredness(sport.gain_tiredness)
      self.notify("sport")
  
    #Fonction pour faire se laver la créature
    def wash(self):
      # Augmentation de la vie
      self.increase_happiness(12)
      self.increase_steps()
      self.increase_health(2)
      #self.increase_physical_health(12)
      
      # Dégradation de la vie
      self.increase_hunger(13)

      self.notify("wash")

    #Fonction pour faire travailler la créature
    def work(self, job: Job):
      self.increase_money(job.salary)
      self.increase_steps()
      self.increase_intelligence(job.gain_intelligence)

      self.decrease_health(job.gain_health)
      self.increase_hunger(job.gain_hunger)
      self.decrease_happiness(job.gain_happiness)
      self.decrease_physical_health(job.gain_physical_health)

      self.notify("work", job)

    #Fonction pour baisser l'intelligence en pourcentage
    def decrease_intelligence(self, amount):
      self._intelligence -= self._intelligence * amount / 100
      if self._intelligence < 0:
        self._intelligence = 0
      self.notify("decrease_intelligence", amount)

    #Fonction pour augmenter l'intelligence en pourcentage
    def increase_intelligence(self, amount):
      self._intelligence += self._intelligence * amount / 100
      if self._intelligence > 100:
        self._intelligence = 100
      self.notify("increase_intelligence", amount)


    def increase_physical_health(self, amount):
      self._physical_health += amount
      if self._physical_health > 100:
        self._physical_health = 100
      self.notify("increase_physical_health", amount)

    def decrease_physical_health(self, amount):
      self._physical_health -= amount
      if self._physical_health < 0:
        self._physical_health = 0
      self.notify("decrease_physical_health", amount)

    #Fonction pour gérer la fatigue
    def increase_tiredness(self, amount):
      self._tiredness += amount
      if self._tiredness > 100:
        self._tiredness = 100
      self.notify("increase_tiredness", amount)
    
    def decrease_tiredness(self, amount):
      self._tiredness -= amount
      if self._tiredness < 0:
        self._tiredness = 0
      self.notify("decrease_tiredness", amount)

    def reset_tiredness(self):
      self._tiredness = 0
    
    #Fonction pour augmenter l'argent
    def increase_money(self, amount):
      self._money += amount
      gain = amount / 100
      self.increase_happiness(gain)
      self.notify("increase_money", amount)

    def decrease_money(self, amount):
      self._money -= amount
      self.decrease_happiness(amount / 10)
      self.notify("decrease_money", amount)

    #Fonction pour augmenter la faim
    def increase_hunger(self, amount):
      self._hunger += amount
      if self._hunger > 100:
        self._hunger = 100
      self.notify("increase_hunger", amount)

    #Fonction pour baisser la faim
    def decrease_hunger(self, amount):
      self._hunger -= amount
      if self._hunger < 0:
        self._hunger = 0
      self.notify("decrease_hunger", amount)
    
    #Fonction pour augmenter la santé
    def increase_health(self, amount):
      self._health += amount
      if self._health > 100:
        self._health = 100
      self.notify("increase_health", amount)

    #Fonction pour baisser la santé
    def decrease_health(self, amount):
      self._health -= amount
      if self._health < 0:
        self._health = 0
      self.notify("decrease_health", amount)

    #Augmentation des étapes de la vie
    # Lorsque les étapes atteignent 16, la créature évolue
    def increase_steps(self):
      self._steps +=1
      if self._steps == 16:
        self._steps = 0
        self.evolve()

    def increase_happiness(self, amount=5):
      self._happiness += amount
      if self._happiness > 100:
        self._happiness = 100
      self.notify("increase_happiness", amount)
    
    def decrease_happiness(self, amount=5):
      self._happiness -= amount
      if self._happiness < 0:
        self._happiness = 0
      self.notify("decrease_happiness", amount)

    def rent(self, amount):
      self.decrease_money(amount) 
      self.notify("rent", amount)

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
      print("\033[1mNom :\033[0m" + self.name)
      print("\033[1mÉtat :\033[0m " + self.state)
      print(" ")
      print("\033[1mHappiness -\033[0m " + self.show_happiness())
      print("\033[1mIntelligence -\033[0m " + self.show_intelligence())
      print("\033[1mFatigue -\033[0m " + self.show_tiredness())
      print("\033[1mFaim -\033[0m " + self.show_hunger())
      print("\033[1mSanté -\033[0m " + self.show_health())
      print("\033[1mSanté physique -\033[0m " + self.show_physical_health())
      print("\033[1mArgent -\033[0m " + self.show_money())
      
    #Fonction pour montrer l'état de la créature
    def show_happiness(self):
        if self._happiness > 80:
            return "Très heureux : " + str(self._happiness) 
        elif self._happiness > 60:
            return "Heureux : " + str(self._happiness)
        elif self._happiness > 40:
            return "Neutre : " + str(self._happiness) 
        elif self._happiness > 20:
            return "Triste : " + str(self._happiness) 
        else:
            return "Très triste : " + str(self._happiness) 

    #Monter l'intelligence de la créature
    def show_intelligence(self):
        if self._intelligence > 40:
            return "Très intelligent : " + str(self._intelligence) 
        elif self._intelligence > 10:
            return "Intelligent : " + str(self._intelligence) 
        elif self._intelligence > 5:
            return "Neutre : " + str(self._intelligence) 
        elif self._intelligence > 3:
            return "Peu intelligent : " + str(self._intelligence) 
        else:
            return "Très peu intelligent : " + str(self._intelligence) 
    
    #Montrer la fatigue de la créature
    def show_tiredness(self):
        if self._tiredness > 80:
            return "Très fatigué : " + str(self._tiredness) 
        elif self._tiredness > 60:
            return "Fatigué : " + str(self._tiredness) 
        elif self._tiredness > 40:
            return "Neutre : " + str(self._tiredness) 
        elif self._tiredness > 20:
            return "Peu fatigué : " + str(self._tiredness) 
        else:
            return "Très peu fatigué : " + str(self._tiredness)

    #Montrer la faim de la créature
    def show_hunger(self):
        if self._hunger > 80:
            return "Très affamé : " + str(self._hunger) 
        elif self._hunger > 60:
            return "Affamé : " + str(self._hunger) 
        elif self._hunger > 40:
            return "Neutre : " + str(self._hunger) 
        elif self._hunger > 20:
            return "Peu affamé : " + str(self._hunger) 
        else:
            return "Très peu affamé : " + str(self._hunger) 
    
    #Montrer la vie de la créature
    def show_health(self):
        if self._health > 80:
            return "Très en bonne santé : " + str(self._health) 
        elif self._health > 60:
            return "En bonne santé : " + str(self._health) 
        elif self._health > 40:
            return "Neutre : " + str(self._health) 
        elif self._health > 20:
            return "En mauvaise santé : " + str(self._health) 
        else:
            return "Très en mauvaise santé : " + str(self._health)
        
    #Montrer la vie physique de la créature
    def show_physical_health(self):
        if self._physical_health > 80:
            return "Très en bonne santé physique : " + str(self._physical_health) 
        elif self._physical_health > 60:
            return "En bonne santé physique : " + str(self._physical_health) 
        elif self._physical_health > 40:
            return "Neutre : " + str(self._physical_health) 
        elif self._physical_health > 20:
            return "En mauvaise santé physique : " + str(self._physical_health) 
        else:
            return "Très en mauvaise santé physique : " + str(self._physical_health)
    
    #Montrer l'argent de la créature
    def show_money(self):
        if self._money > 80:
            return "Très riche : " + str(self._money) 
        elif self._money > 60:
            return "Riche : " + str(self._money) 
        elif self._money > 40:
            return "Neutre : " + str(self._money) 
        elif self._money > 20:
            return "Pauvre : " + str(self._money) 
        else:
            return "Très pauvre : " + str(self._money)

    def is_alive(self):
      return self._health > 0
    
    def die(self):
      self._health = 0
      self.notify("die")

    def score(self):
      score = 0
      score += self._happiness * 2
      score += self._money / 100
      score += round(self._intelligence) / 2
      score += self._health
      score += self._physical_health * 2

      score -= self._hunger * 5
      score -= self._tiredness * 5
      return score
