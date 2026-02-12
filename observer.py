class Observer:
    def update(self, subject, event, amount=None):
        if event == "eat":
            print(f"{subject.name} a mangé et a maintenant {subject.hunger} de faim")
        
        elif event == "sleep":
            print(f"{subject.name} a dormi")

        elif event == "study":
            print(f"{subject.name} a étudié et a maintenant {subject.intelligence} d'intelligence")

        elif event == "play":
            print(f"{subject.name} a joué et a maintenant {subject.happiness} de bonheur")

        elif event == "sport":
            print(f"{subject.name} a fait du sport et a maintenant {subject.health} de santé")

        elif event == "wash":
            print(f"{subject.name} s'est lavé et a maintenant {subject.health} de santé et {subject.happiness} de bonheur")

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
