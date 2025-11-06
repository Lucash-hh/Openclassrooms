import random
from time import sleep

def jeu_du_pendu():
    with open('francais.txt', 'r', encoding='utf-8') as fichier:
        mot = [mot.strip() for mot in fichier.readlines() if mot.strip()]
    ordinateur = random.choice(mot)

    long = ""
    essais = 8

    for i in range(len(ordinateur)):
        long = long + "_"

    lettrees_trouvees = [long]
    mauvaise_lettres = []

    print("---Jeu du pendu---")
    sleep(1)
    print("Vous avez 8 essais !")
    sleep(1)
    print(f"Trouvez les bonnes lettres : {" ".join(long)}")
    sleep(1)

    while True :
        lettre = str(input("Entrez une lettre : ")).lower().strip()

        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre\n")
            continue

        if lettre in lettrees_trouvees or lettre in mauvaise_lettres:
            print("Vous avez déjà proposé cette lettre\n")
            mauvaise_lettres.append(lettre)
            print(mauvaise_lettres)
            continue

        if lettre in ordinateur:
            lettrees_trouvees.append(lettre)

        else:
            essais -= 1
            print("-1 essai")
            print(f"Il vous en reste {essais}\n")
            mauvaise_lettres.append(lettre)
        
        affichage = " ".join(l if l in lettrees_trouvees else "_" for l in ordinateur)
        print(affichage)

        if essais == 0:
            print(f"Vous êtes pendu :( le mot était : {ordinateur}")
            break

        if "_" not in affichage :
            print("Vous êtes sauvé :D !")
            break

while True:
    jeu_du_pendu()
    jouer = input("Rejouez ? Y/N ").lower().strip()

    if jouer != "y":
        print("Goodbye")

        break
