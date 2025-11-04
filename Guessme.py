import random
from time import sleep

nombre_mystère = random.randint(1,100)

essais = 0

print("Trouvez le nombre mystère entre 1 et 100 !")
sleep(0.5)

while True:
    try:
        choix = int(input("Entrez un nombre : "))
    except ValueError:
        print("Ce n'est pas un nombre entier...")
        continue
    print("Loading..")
    sleep(1.5)

    essais += 1

    if choix == nombre_mystère:
        print(f"Vous avez gagner en {essais} essais !")
        break
    elif choix < nombre_mystère:
        print("Trop petit !")
    elif choix > nombre_mystère:
        print("Trop grand !")
    elif essais >= 10:
        print("La persévérance est un grand atout")