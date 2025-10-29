def voir_taches():
    with open ('taches.txt', 'r') as f:
        contenu = f.read()
    print(contenu)

def ajouter_taches():
    contenu = str(input("Ajouter une nouvelle tâche : "))

    try:
        with open('taches.txt', 'r') as f:
            lignes = f.readlines()
            numero = len(lignes) + 1
    except FileNotFoundError:
        numero = 1

    with open('taches.txt', 'a') as f:
        f.write(f"{numero}. {contenu}\n")
    
    print("---Nouvelle tâche ajoutée---")

def marquer_tâche_comme_terminee():
    voir_taches()
    choix = int(input("Entrez le numéro de la tâche : "))

    with open('taches.txt', 'r') as f:
        lignes = f.readlines()

    if 1 <= choix <= len(lignes):
        lignes[choix - 1] = lignes[choix - 1].strip() + ".TERMINER\n"

        with open('taches.txt', 'w') as f:
            f.writelines(lignes)
        print("---Tâche terminer---")

    else:
        print("Numéro invalide.")

def supprimer_une_tache():
    voir_taches()
    with open('taches.txt', 'r') as f:
        lignes = f.readlines()

    try:
        choix = int(input("Entrez le numéro de la tâche à supprimer : "))
    except ValueError:
        print("Numéro invalide.")
        return

    if 1 <= choix <= len(lignes):
        del lignes[choix - 1]

        with open('taches.txt', 'w') as f:
            for i, ligne in enumerate(lignes, start = 1):
                ligne_sans_num = ligne.split('. ', 1)[-1]
                f.write(f"{i}. {ligne_sans_num.strip()}\n")

        print("---Tâche supprimée---")
    
    else:
        print("Numéro invalide.")

while True:

    print("1. Voir les tâches")
    print("2. Ajouter une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Supprimer une tâche")
    print("5. Quitter")

    choix = int(input("Sélectionner votre choix, 1/2/3/4/5 : "))

    if choix == 5:
        print("Aurevoir")
        break
    elif choix == 1:
        voir_taches()
    elif choix == 2:
        ajouter_taches()
    elif choix == 3:
        marquer_tâche_comme_terminee()
    elif choix == 4:
        supprimer_une_tache()