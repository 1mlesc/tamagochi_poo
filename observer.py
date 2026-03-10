class Observer():
    def update(self, subject, event, amount=None):
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
            print("      _______       |\__/,|   (`\ "
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
            print("    /\_/\ "
                "\n   ( o.o )"
                "\n   >  ^  <"
                "\n  /  ___  \ "
                "\n (__/   \__)")

        elif event == "wash":
            print(f"{subject.name} s'est lavé et a maintenant {subject.health} de santé et {subject.happiness} de bonheur")
            print(" ")
            print("   /\_/\ "
                "\n  ( >.< )"
                "\n  (  u  )"
                "\n  /     \ "
                "\n |       |")
        
        elif event == "work":
            print(f"{subject.name} a fini de travailler")
            print(" ")
            print("   /\_/\ "
                "\n  ( x.x )"
                "\n   > ' <"
                "\n  /  ~  \ "
                "\n (_______)"
                "\n |_|___|_|")
        
        # Notifications for attribute changes (increase / decrease)
        elif event == "increase_intelligence":
            print(f"{subject.name} a gagné \033[1m{amount}% d'intelligence\033[0m")
        elif event == "decrease_intelligence":
            print(f"{subject.name} a perdu \033[1m{amount}% d'intelligence\033[0m")
        elif event == "increase_physical_health":
            print(f"{subject.name} a augmenté sa \033[1msanté physique de {amount}\033[0m")
        elif event == "decrease_physical_health":
            print(f"{subject.name} a diminué sa \033[1msanté physique de {amount}\033[0m")
        elif event == "increase_tiredness":
            print(f"{subject.name} s'est \033[1mfatigué de {amount}\033[0m")
        elif event == "decrease_tiredness":
            print(f"{subject.name} a récupéré de \033[1m{amount} de fatigue\033[0m")
        elif event == "increase_money":
            print(f"{subject.name} a gagné \033[1m{amount}€\033[0m")
        elif event == "decrease_money":
            print(f"{subject.name} a perdu \033[1m{amount}€\033[0m")
        elif event == "increase_hunger":
            print(f"{subject.name} a \033[1mfaim de +{amount}\033[0m")
        elif event == "decrease_hunger":
            print(f"{subject.name} a \033[1mmoins faim de -{amount}\033[0m")
        elif event == "increase_health":
            print(f"{subject.name} a gagné \033[1m{amount} de santé\033[0m")
        elif event == "decrease_health":
            print(f"{subject.name} a perdu \033[1m{amount} de santé\033[0m")
        elif event == "increase_happiness":
            print(f"{subject.name} est \033[1mplus heureux de +{amount}\033[0m")
        elif event == "decrease_happiness":
            print(f"{subject.name} est\033[1m moins heureux de -{amount}\033[0m")
        elif event == "rent":
            print(f"{subject.name} a \033[1mpayé {amount}€ de loyer\033[0m !")
        elif event == "need_sleep":
            print(f"{subject.name} est \033[1mtrès fatigué\033[0m, il doit aller dormir ! -1 action possible")
        elif event == "need_food":
            print(f"{subject.name} est \033[1mtrès affamé\033[0m, il doit aller manger ! -1 action possible")
        elif event == "die":
            print(f"{subject.name} est \033[1m\033[4mmort\033[0m !")
        elif event == "evolve_kid":
            print(" ")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print(f"{subject.name} a évolué en \033[1mEnfant\033[0m ! Félicitations, il peut désormais étudier et faire du sport !")
            print(" ")
            print("   /\_/\ "
                "\n  ( o.o )         i   i"
                "\n   > ^ <        __|___|__"
                "\n  /  ~  \      |~~~Cake~~|"
                "\n (       )     |_________|")
            print("---------------------------------------------------------------------------------------------------------------------------")
        elif event == "evolve_adult":
            print(" ")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print(f"{subject.name} a évolué en \033[1mAdulte\033[0m ! Félicitations, il peut désormais travailler !")
            print(" ")
            print("   /\___/\ "
                "\n  (  o o  )"
                "\n  /  =^=  \       i   i"
                "\n (   ''    )    __|___|__"
                "\n  \_______/    |~~~Cake~~|"
                "\n   |  |  |     |_________|")
            print("---------------------------------------------------------------------------------------------------------------------------")
        elif event == "evolve_old":
            print(" ")
            print("---------------------------------------------------------------------------------------------------------------------------")
            print(f"{subject.name} a évolué en \033[1mVieux\033[0m !")
            print(" ")
            print("    /\_/\ "
                "\n   ( -.- )        i   i"
                "\n   /  '  \  //  __|___|__"
                "\n  (   _   )//  |~~~Cake~~|"
                "\n /| /   \ |/   |_________|")
            print("---------------------------------------------------------------------------------------------------------------------------")

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