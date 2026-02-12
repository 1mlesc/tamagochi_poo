class Observer:
    def update(self, subject, event, amount=None):
        if event == "eat":
            print(f"{subject.name} a fini de manger")
        
        elif event == "sleep":
            print(f"{subject.name} a dormi")

        elif event == "study":
            print(f"{subject.name} a fini d'étudier")

        elif event == "play":
            print(f"{subject.name} a fini de jouer")

        elif event == "sport":
            print(f"{subject.name} a fini son sport")

        elif event == "wash":
            print(f"{subject.name} a fini de se laver")
        elif event == "work":
            print(f"{subject.name} a fini de travailler")
        # Notifications for attribute changes (increase / decrease)
        elif event == "increase_intelligence":
            print(f"{subject.name} a gagné {amount}% d'intelligence")
        elif event == "decrease_intelligence":
            print(f"{subject.name} a perdu {amount}% d'intelligence")
        elif event == "increase_physical_health":
            print(f"{subject.name} a augmenté sa santé physique de {amount}")
        elif event == "decrease_physical_health":
            print(f"{subject.name} a diminué sa santé physique de {amount}")
        elif event == "increase_tiredness":
            print(f"{subject.name} s'est fatigué de {amount}")
        elif event == "decrease_tiredness":
            print(f"{subject.name} a récupéré de {amount} de fatigue")
        elif event == "increase_money":
            print(f"{subject.name} a gagné {amount}€")
        elif event == "decrease_money":
            print(f"{subject.name} a perdu {amount}€")
        elif event == "increase_hunger":
            print(f"{subject.name} a faim de +{amount}")
        elif event == "decrease_hunger":
            print(f"{subject.name} a moins faim de -{amount}")
        elif event == "increase_health":
            print(f"{subject.name} a gagné {amount} de santé")
        elif event == "decrease_health":
            print(f"{subject.name} a perdu {amount} de santé")
        elif event == "increase_happiness":
            print(f"{subject.name} est plus heureux de +{amount}")
        elif event == "decrease_happiness":
            print(f"{subject.name} est moins heureux de -{amount}")
        elif event == "evolve_adult":
            print(f"{subject.name} a évolué en Adulte !")
        elif event == "evolve_old":
            print(f"{subject.name} a évolué en Vieux !")
        elif event == "rent":
            print(f"{subject.name} a payé {amount}€ de loyer !")
        elif event == "need_sleep":
            print(f"{subject.name} est très fatigué, il doit aller dormir ! -1 action possible")
        elif event == "need_food":
            print(f"{subject.name} est très affamé, il doit aller manger ! -1 action possible")
        elif event == "die":
            print(f"{subject.name} est mort !")
        elif event == "evolve_kid":
            print(f"{subject.name} a évolué en Enfant ! Félicitations, il peut désormais étudier et faire du sport !")
            print(
    "\n      __"
        "\n     (  )"
      "\n      )("
    "\n   ,;/  \:."
   "\n  ( `.__,' )"
    "\n   `-.__,-'"
     "\n    ((__))"
"\n     `--'")
    

class Observable:
    def __init__(self):
        self._observers = []

    #Ajouter un observateur
    def add_observer(self, observer):
        self._observers.append(observer)

    #Supprimer un observateur
    def remove_observer(self, observer):
        self._observers.remove(observer)

    #Notifier les observateurs d'un événement
    def notify(self, event, amount=None):
      for observer in self._observers:
        observer.update(self, event, amount)
