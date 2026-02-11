from creature import Creature

class Factory:
   
   def create_creature(self, name, happiness=50, intelligence=1, tiredness=30, hunger=30, health=100, state="Bébé", money=0):
      return Creature(name, happiness, intelligence, tiredness, hunger, health, state, money)