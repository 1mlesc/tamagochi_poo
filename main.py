from factory import Factory
import questionary

from food import Food
from job import Job
from observer import GameUI
from play import Play
from study import Study
from sport import Sport

creature = Factory().create_creature("Tom")
creature.add_observer(GameUI())

def rules():
    creature.notify("rule")

def end_game():
    print("Fin du jeu !! Voici vos stats de votre créature :")
    creature.show_status() 
    print("Score final : " + str(creature.score()))
    print("Merci d'avoir joué !")

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
can_die = False
    
#Boucle du jeu
rules()
while creature.is_alive():
    j = 9
    while j != 11:
        #Paiement du loyer lorsqu'on est adulte ou vieux
        if creature.state == adult or creature.state == old:
            creature.rent(400)
        #Vérification de la santé de la créature, si elle est trop basse, elle meurt
        if can_die == True:
            creature.show_status()
            creature.die()
        if creature.state == (baby or kid or adult or old) and creature._happiness < 15 or creature._health < 15 or creature._hunger > 85:
            print("Votre créature n'est pas au meilleur de sa forme, à la fin de la journée, elle pourrait en mourir !")
            can_die = True
        else:
            can_die = False
            j +=1
        i = 0
        while i != actions_possible:
            #Si la créature est très fatiguée, on lui enlève une action possible
            if creature._tiredness > 90:
                creature.notify("need_sleep")
                i+= 1
            #Si la créature est très affamée, on lui enlève une action possible
            if creature._hunger > 90:
                creature.notify("need_food")
                i+= 1

            print(" ")
            print("\033[1m\033[4mJour " + str(j) + " :\033[0m")
            print("Actions restantes : " + str(actions_possible - i))
            print(" ")
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
                creature.notify("sleep")
            #Action Étudier
            elif action == "Étudier":
                study_action = questionary.select(
                    "Que veux-tu qu'il étudie ?",
                    choices=[study.name for study in Study.get_studies_by_intelligence(creature._intelligence)]
                ).ask()
                study_action = next(study for study in Study.get_studies_by_intelligence(creature._intelligence) if study.name == study_action)
                creature.study(study_action)
            #Action Jouer
            elif action == "Jouer":
                play_action = questionary.select(
                    "Avec quoi veux-tu qu'il joue ?", 
                    choices=[play.name for play in Play.get_plays_by_intelligence(creature._intelligence)] 
                ).ask() 
                play_action = next(play for play in Play.get_plays_by_intelligence(creature._intelligence) if play.name == play_action) 
                creature.play(play_action) 
            elif action == "Travailler":
                job_action = questionary.select(
                    "Quel travail voulez-vous lui faire faire ?",
                    choices=[job.name for job in Job.get_jobs_by_state(creature._intelligence)]
                ).ask()
                job_action = next(job for job in Job.get_jobs_by_state(creature._intelligence) if job.name == job_action)
                creature.work(job_action)
            #Action Faire du sport
            elif action == "Faire du sport":
                sport_action = questionary.select(
                    "Quel sport voulez-vous qu'il fasse ?",
                    choices=[sport.name for sport in Sport.get_sports_by_physical_health(creature._physical_health)]
                ).ask()
                sport_action = next(sport for sport in Sport.get_sports_by_physical_health(creature._physical_health) if sport.name == sport_action) 
                creature.sport(sport_action)
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
            creature.notify("bigSleep")

        j += 1
        creature.show_status()
        #Lorsque nous sommes au jour 10, fin du jeu, on montre les résultats
        if j == 10:
            creature.die()
            break


end_game()


    