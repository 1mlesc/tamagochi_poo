from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject, event, amount=None):
        pass

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