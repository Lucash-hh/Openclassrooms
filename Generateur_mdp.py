import random
import string

def generer_mdp(a, exclude_problematic_punct=True):
    ponctuation = string.punctuation
    if exclude_problematic_punct:
         for c in ['"', "'", "\\", "`"]:
              ponctuation = ponctuation.replace(c, "")
    
    caracteres = string.ascii_letters + string.digits + ponctuation

    mdp = ''.join(random.choice(caracteres) for _ in range(a))
    return mdp

while True:
    try:
        choix = int(input("Entrez le nombre de caractère du mdp min : 8 max : 60 où [0] pour quitter : "))
    except ValueError:
        print("Nombre de carractère invalide.")
        continue
    if 8 <= choix <= 60:
            print(f"Voici votre mot de passe : {generer_mdp(choix)}")
    elif choix == 0:
         break
    else:
         print("Nombre de caractères minimum 8 maximum 60")