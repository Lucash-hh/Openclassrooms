import random
import keyboard
from time import sleep

des = [1,2,3,4,5,6]

print("lancés les dés et fait mieux que l'ordinateur !")

def lancer():
    A = random.choice(des)
    B = random.choice(des)
    total_ordinateur = A + B
    print(f"{total_ordinateur} faite mieux..\n")
    print("Chargement...\n")
    sleep(1)

    C = random.choice(des)
    print(f"{C} et...\n")
    sleep(1)
    D = random.choice(des)
    print(f"{D} !\n")

    total = C + D

    if total > total_ordinateur:
        print("Bien jouer !")
    elif total == total_ordinateur:
        print("Egaliter !")
    else:
        print("Perdu !")

while True :
    print("Appuyez sur espace pour lancer les dés !")
    keyboard.wait("space")
    lancer()

    print("Rejouer ? Y/N")
    key = keyboard.read_key().lower()

    if key == "y":
        continue
    elif key == "n":
        print("Aurevoir")
        break