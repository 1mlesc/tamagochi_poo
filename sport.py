class Sport:
    def __init__(self, name, physical_health, gain_physical_health, gain_happiness=1, gain_hunger=1, gain_tiredness=1):
        self.name = name
        self.physical_health = physical_health
        self.gain_physical_health = gain_physical_health
        self.gain_happiness = gain_happiness
        self.gain_hunger = gain_hunger
        self.gain_tiredness = gain_tiredness

    def get_sports_by_physical_health(physical_health):
        sports = sorted([course, natation, musculation, yoga, danse], key=lambda x: x.physical_health) 
        return [sport for sport in sports if sport.physical_health <= physical_health] 


course = Sport("Course", 10, gain_physical_health=8,gain_happiness=5, gain_hunger=5, gain_tiredness=10) 
natation = Sport("Natation",30, gain_physical_health=10,gain_happiness=10, gain_hunger=10, gain_tiredness=20) 
musculation = Sport("Musculation", 50, gain_physical_health=12,gain_happiness=15, gain_hunger=15, gain_tiredness=30) 
yoga = Sport("Yoga", 70, gain_physical_health=14,gain_happiness=17, gain_hunger=20, gain_tiredness=40)
danse = Sport("Danse", 90, gain_physical_health=17,gain_happiness=25, gain_hunger=25, gain_tiredness=50)