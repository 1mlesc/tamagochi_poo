from factory import Factory
import questionary

from food import Food
from study import Study

creature = Factory().create_creature("Tom")

def rules():
    print("Bienvenue dans le jeu de Tamagochi !")
    print("Votre créature s'appelle " + creature.name + " et elle est actuellement un " + creature.state + ".")
    print("Vous pouvez faire les actions suivantes : Manger, Dormir, Se laver, Jouer, Étudier, Faire du sport, Travailler en fonction de l'état de votre créature.")
    print("Chaque action a des effets différents sur votre créature. Par exemple, manger baisse la faim, dormir réduit la fatigue, étudier augmente l'intelligence, etc.")
    print("Votre objectif est de prendre soin de votre créature et de la faire évoluer en lui faisant faire les bonnes actions au bon moment !")
    print("Chaque action que vous faites augmente les étapes de la vie de votre créature. Lorsque les étapes atteignent 8, votre créature évolue et passe à l'état suivant !")
    print("But du jeu : faire évoluer votre créature jusqu'à l'état de Vieux en prenant soin d'elle et en lui faisant faire les bonnes actions au bon moment !")



actions_possible = 5

choices = [
    "Manger",
    "Dormir",
    "Se laver",
    "Jouer",
]

if creature.state == "Enfant":
    choices.append("Étudier", "Faire du sport")
elif creature.state == "Adulte":
    choices.append("Étudier", "Faire du sport", "Travailler")
elif creature.state == "Vieux":
    choices.append("Faire du sport", "Travailler", "Se reposer")


while creature.is_alive():
    j= 1
    while j != 10:
      i = 0
      while i != actions_possible:
        print("Jour " + str(j) + " :")
        print("Actions possibles : " + str(actions_possible))
        action = questionary.select(
            "Que voulez-vous faire ?",
            choices=choices
        ).ask()
        #Action Manger
        if action == "Manger":
            eat_action = questionary.select(
                "Que voulez-vous lui faire manger ?",
                choices=Food.get_foods_by_state(creature.state)
            ).ask()
            creature.eat(eat_action)
        #Action Dormir
        elif action == "Dormir":
            creature.sleep()
        #Action Étudier
        elif action == "Étudier":
            study_action = questionary.select(
                "Que veux-tu qu'il étudie ?",
                choices=Study.get_studies_by_state(creature.state)
            ).ask()
            creature.study(study_action)
        #Action Jouer
        elif action == "Jouer":
            pass
        #Action Faire du sport
        elif action == "Faire du sport":
            pass
        #Action Travailler
        elif action == "Se laver":
            creature.wash()
      i +=1
    #Lorsqu'on a plus d'action possibles, on dort !
    action = questionary.select(
      "On est le soir, on doit aller dormir !!",
      choices= "Dormir"
    ).ask()
    if action == "Dormir":
          creature.sleep()

    print(creature.show_happiness())
      
    j += 1

    