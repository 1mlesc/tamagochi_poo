class Play:
    def __init__ (self, name, gain=100, intelligence=1, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1):
        self.name = name
        self.gain = gain
        self.intelligence = intelligence
        self.gain_happiness = gain_happiness
        self.gain_hunger = gain_hunger 
        self.gain_tiredness = gain_tiredness
        self.gain_intelligence = gain_intelligence

    def get_plays_by_intelligence(intelligence):
        plays= []
        temp_plays = [petiteBalle, ballon, balleTennis, ballonFoot, ballonBasket, ballonRugby, poupée, voiture, peluche, lego, puzzle, carte, console] 
        for play in temp_plays: 
            if play.intelligence <= intelligence: 
                plays.append(play) 
        return plays
    
#Création de jouets
    #Ballon :
    #   BAsique
petiteBalle = Play("Petite balle", 5, 0, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
ballon = Play("Ballon", 5, 0, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
    #   Amélioration
balleTennis = Play("Balle de tennis", 10, 5, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
ballonFoot = Play("Ballon de foot", 10, 5, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
ballonBasket = Play("Ballon de basket", 15, 10, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
ballonRugby = Play("Ballon de rugby", 20, 15, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)

poupée = Play("Poupée", 10, 5, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
voiture = Play("Voiture", 10, 5, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
peluche = Play("Peluche", 15, 8, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
lego = Play("Lego", 15, 10, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
puzzle = Play("Puzzle", 25, 15, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
carte = Play("Carte", 35, 20, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)
console = Play("Console", 35, 20, gain_happiness=1, gain_hunger=1, gain_tiredness=1, gain_intelligence=1)