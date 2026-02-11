class Creature:
    def __init__(self, name, happiness=50, intelligence=1, tiredness=30, hunger=30, health=100, state="Bébé", money=0):
      self.name = name
      self.state = state
      self.happiness = happiness
      self.intelligence = intelligence
      self.tiredness = tiredness
      self.hunger = hunger
      self.health = health
      self.physical_health = health
      self.money = money


    #Fonction pour faire manger la créature
    def eat(self):
      pass


    #Fonction pour faire dormir la créature
    def sleep(self):
      pass


    #Fonction pour faire étudier la créature
    def study(self, subject):
      intelligence_gain = subject.gain
      self.intelligence += self.intelligence * (intelligence_gain / 100)
      return self.intelligence

    #Fonction pour faire jouer la créature
    def play(self):
      pass

    #Fonction pour faire faire du sport à la créature
    def sport(self):
      pass
  
    #Fonction pour faire se laver la créature
    def wash(self):
      pass

    #Fonction pour faire travailler la créature, plus la créature est intelligente, plus elle gagne de l'argent et du bonheur
    def work(self):
      pass

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

