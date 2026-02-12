from creature import Creature

class Factory:
   
   def create_creature(self, name, happiness=30, intelligence=2, tiredness=60, hunger=60, health=80, state="Bébé", money=0, steps=0):
      return Creature(name, happiness, intelligence, tiredness, hunger, health, state, money)