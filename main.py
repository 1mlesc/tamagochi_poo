from factory import Factory
import questionary


creature = Factory().create_creature("Tamagochi")

print("Bienvenue dans le jeu de Tamagochi !")
print("Votre créature s'appelle " + creature.name + " et elle est actuellement un " + creature.state + ".")

jour = 1
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
        print("Jour " + str(jour) + " :")
        print("Actions possibles : " + str(actions_possible))
        action = questionary.select(
            "Que voulez-vous faire ?",
            choices=choices
        ).ask()

        if action == "Manger":
            pass
        elif action == "Dormir":
            pass
        elif action == "Étudier":
            pass
        elif action == "Jouer":
            pass
        elif action == "Faire du sport":
            pass
        elif action == "Se laver":
            pass

        print(creature.show_happiness())
        i +=1
      j += 1

    