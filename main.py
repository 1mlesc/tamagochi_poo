from factory import Factory
import questionary

from food import Food
from job import Job
from observer import Observer
from study import Study

creature = Factory().create_creature("Tom")
creature.add_observer(Observer())

def rules():
    print("Bienvenue dans le jeu de Tamagochi !")
    print("Votre créature s'appelle " + creature.name + " et elle est actuellement un " + creature.state + ".")
    print("Vous pouvez faire les actions suivantes : Manger, Dormir, Se laver, Jouer, Étudier, Faire du sport, Travailler en fonction de l'état de votre créature.")
    print("Chaque action a des effets différents sur votre créature. Par exemple, manger baisse la faim, dormir réduit la fatigue, étudier augmente l'intelligence, etc.")
    print("Votre objectif est de prendre soin de votre créature et de la faire évoluer en lui faisant faire les bonnes actions au bon moment !")
    print("Chaque action que vous faites augmente les étapes de la vie de votre créature. Lorsque les étapes atteignent 8, votre créature évolue et passe à l'état suivant !")
    print("But du jeu : faire évoluer votre créature jusqu'à l'état de Vieux en prenant soin d'elle et en lui faisant faire les bonnes actions au bon moment !")


baby = "Bébé"
kid = "Enfant"
adult = "Adulte"
old = "Vieux"

actions_possible = 5

choices_baby = [
    "Manger",
    "Dormir",
    "Se laver",
    "Jouer",
]
choices_kid = [
    "Manger",
    "Dormir",
    "Étudier",
    "Faire du sport",
    "Se laver",
    "Jouer",
]

choices_adult = [
    "Manger",
    "Dormir",
    "Étudier",
    "Faire du sport",
    "Se laver",
    "Travailler",
    "Jouer",
]
choices_old = [
    "Manger",
    "Dormir",
    "Se laver",
    "Travailler",
]

    

rules()
while creature.is_alive():
    j= 1
    while j != 10:
        i = 0
        while i != actions_possible:
            print("Jour " + str(j) + " :")
            print("Actions restantes : " + str(actions_possible - i))
            action = questionary.select(
                "Que voulez-vous faire ?",
                choices=choices_baby if creature.state == baby else choices_kid if creature.state == kid else choices_adult if creature.state == adult else choices_old
            ).ask()
            #Action Manger
            if action == "Manger":
                eat_action = questionary.select(
                    "Que voulez-vous lui faire manger ?",
                    choices=[food.name for food in Food.get_foods_by_state(creature.state)]
                ).ask()
                eat_action = next(food for food in Food.get_foods_by_state(creature.state) if food.name == eat_action)
                creature.eat(eat_action)
            #Action Dormir
            elif action == "Dormir":
                creature.sleep()
            #Action Étudier
            elif action == "Étudier":
                study_action = questionary.select(
                    "Que veux-tu qu'il étudie ?",
                    choices=[study.name for study in Study.get_studies_by_state(creature.state)]
                ).ask()
                study_action = next(study for study in Study.get_studies_by_state(creature.state) if study.name == study_action)
                creature.study(study_action)
            #Action Jouer
            elif action == "Jouer":
                pass
            elif action == "Travailler":
                job_action = questionary.select(
                    "Quel travail voulez-vous lui faire faire ?",
                    choices=[job.name for job in Job.get_jobs_by_state(creature.intelligence)]
                ).ask()
                job_action = next(job for job in Job.get_jobs_by_state(creature.intelligence) if job.name == job_action)
                creature.work(job_action)
            #Action Faire du sport
            elif action == "Faire du sport":
                pass
            #Action Travailler
            elif action == "Se laver":
                creature.wash()
            i +=1
        #Lorsqu'on a plus d'action possibles, on dort !
        action = questionary.select(
        "On est le soir, on doit aller dormir !",
        choices= ["Dormir"]
        ).ask()
        if action == "Dormir":
            creature.sleep()

        j += 1
        print(creature.show_status())
      
    

    