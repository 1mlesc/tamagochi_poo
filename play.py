class Play:
    def __init__ (self, name, gain=1, intelligence=0, gain_happiness=5, gain_hunger=3, gain_tiredness=3, gain_intelligence=0):
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
    
    #Création de jouets (valeurs plus signifiantes)
    #Ballon :
    #   BAsique
petiteBalle = Play("Petite balle", 1, 0, gain_happiness=6, gain_hunger=5, gain_tiredness=5, gain_intelligence=3)
ballon = Play("Ballon", 1, 0, gain_happiness=6, gain_hunger=5, gain_tiredness=8, gain_intelligence=3)
    #   Amélioration
balleTennis = Play("Balle de tennis", 1, 5, gain_happiness=8, gain_hunger=10, gain_tiredness=10, gain_intelligence=4)
ballonFoot = Play("Ballon de foot", 1, 5, gain_happiness=8, gain_hunger=10, gain_tiredness=10, gain_intelligence=4)
ballonBasket = Play("Ballon de basket", 1, 10, gain_happiness=10, gain_hunger=10, gain_tiredness=10, gain_intelligence=4)
ballonRugby = Play("Ballon de rugby", 1, 15, gain_happiness=10, gain_hunger=10, gain_tiredness=10, gain_intelligence=4)

poupée = Play("Poupée", 1, 5, gain_happiness=7, gain_hunger=12, gain_tiredness=12, gain_intelligence=5)
voiture = Play("Voiture", 1, 5, gain_happiness=7, gain_hunger=12, gain_tiredness=12, gain_intelligence=5)
peluche = Play("Peluche", 1, 8, gain_happiness=9, gain_hunger=12, gain_tiredness=12, gain_intelligence=5)
lego = Play("Lego", 1, 10, gain_happiness=10, gain_hunger=13, gain_tiredness=14, gain_intelligence=5)
puzzle = Play("Puzzle", 1, 15, gain_happiness=12, gain_hunger=13, gain_tiredness=14, gain_intelligence=5)
carte = Play("Carte", 1, 20, gain_happiness=12, gain_hunger=13, gain_tiredness=14, gain_intelligence=5)
console = Play("Console", 1, 20, gain_happiness=15, gain_hunger=15, gain_tiredness=18, gain_intelligence=5)