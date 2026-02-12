from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
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
        if observer not in self._observers:
            self._observers.append(observer)

    #Supprimer un observateur
    def remove_observer(self, observer):
        self._observers.remove(observer)

    #Notifier les observateurs d'un événement
    def notify(self, event, amount=None):
      for observer in self._observers:
        observer.update(self, event, amount)

class GameUI(Observer):
    @staticmethod
    def update(subject, event, amount=None):
        if event == "rule":
            print("                                            ,''`."
                  "\n                                           /     \ "
                  "\n                                          :\/\/\/\:"
                  "\n                                          :       :"
                  "\n Bienvenue dans le jeu de Tamagochi !      `.___,'")
            print(f"Votre créature s'appelle \033[1m{subject.name}\033[0m et elle est actuellement un \033[1m{subject.state}\033[0m.")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("Vous pouvez faire les actions suivantes :")
            print(" \033[1mManger, Dormir, Se laver, Jouer, Étudier, Faire du sport, Travailler\033[0m en fonction de l'état de votre créature.")
            print("Chaque action a des effets différents sur votre créature. Par exemple, manger baisse la faim, dormir réduit la fatigue, étudier augmente l'intelligence, etc.")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("Votre objectif est de prendre \033[1msoin\033[0m de votre créature et de la faire \033[1mévoluer\033[0m en lui faisant faire les bonnes actions au bon moment !")
            print("Chaque action que vous faites augmente les étapes de la vie de votre créature.")
            print("Lorsque les étapes atteignent 8, votre créature évolue et passe à l'état suivant !")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print("\033[1m\033[4mBut du jeu :\033[1m faire évoluer votre créature jusqu'à l'état de \033[1mVieux\033[0m en prenant soin d'elle et en lui faisant \033[1mfaire les bonnes actions au bon moment !\033[0m")
        
        elif event == "eat":
            print(f"{subject.name} a mangé et a maintenant {subject.hunger} de faim")
            print(" ")
            print("     /\_____/\ "
               "\n    /  o   o  \ "
               "\n   ( ==  ^  == )"
               "\n    )         ("
               "\n   (           )"
               "\n  ( (  )   (  ) )"
               "\n (__(__)___(__)__)")
        
        elif event == "sleep":
            print(f"{subject.name} a fait une sieste")
            print("      _"
                  "\n  |\_'/-..--."
                  "\n / _ _   ,  ;"
                  "\n`~=`Y'~_<._./"
                  "\n <`-....__.' ")

        elif event == "bigSleep":
            print("Tom est parti dormir pour la nuit...")
            print(" ")
            print("        |\      _,,,---,,_"
                "\n ZZZzz /,`.-'`'    -.  ;-;;,_"
                "\n      |,4-  ) )-,_. ,\ (  `'-'"
                "\n      '---''(_/--'  `-'\_)")
            print("---------------------------------------------------")

        elif event == "study":
            print(f"{subject.name} a étudié et a maintenant {subject.intelligence} d'intelligence")
            print(" ")
            print("           _______      |\__/,|   (`\ "
                    "\n     /       /_   _.|o o  |_   ) )"
                    "\n    /       / /  -(((---(((--------"
                    "\n   /       / /"
                    "\n  /_______/ /"
                    "\n ((______| /")

        elif event == "play":
            print(f"{subject.name} a joué et a maintenant {subject.happiness} de bonheur")
            print(" ")
            print("     /\_/\           ___"
                "\n    = o_o =_______    \ \ "
                "\n     __^      __(  \.__) )"
                "\n (@)<_____>__(_____)____/")

        elif event == "sport":
            print(f"{subject.name} a fait du sport et a maintenant {subject.health} de santé")
            print(" ")
            print("  /\_/\ "
                "\n ( o.o )"
                "\n >  ^  <"
               "\n /  ___  \ "
              "\n (__/   \__)")

        elif event == "wash":
            print(f"{subject.name} s'est lavé et a maintenant {subject.health} de santé et {subject.happiness} de bonheur")
            print(" ")
            print("  /\_/\ "
                "\n ( >.< )"
                "\n (  u  )"
                "\n /     \ "
               "\n|       |")