import requests

url = "https://open.er-api.com/v6/latest/EUR"
reponse = requests.get(url)
data = reponse.json()

taux_usd = data['rates']['USD']

print("-----Convertisseur-----")
print(f"--1 EUR = {taux_usd:.2f} USD--")
print(f"--1 USD = {1/taux_usd:.2f} EUR--\n")

while True:
    print("Option [1] EUR -> USD")
    print("Option [2] USD -> EUR")
    print("Option [0] -> QUITTER\n")
    try:
        option = int(input("Choisissez une option : [0] [1] [2] "))

    except ValueError:
        print("Veuillez entrer une option valide.\n")
        continue

    if option == 0:
        break

    elif option == 1:
        while True:
            try:
                choix_euro = float(input("Entrez un montant en euros : "))
                if choix_euro == 0:
                    break
                elif choix_euro < 0:
                    print("Nombre Incorrect\n")
                    continue

                print(f"{choix_euro} EUR =  {choix_euro * taux_usd:.2f} USD\n")
                print("Revenir au menu principal [0]")
            except ValueError:
                print("Nombre incorrect\n")
                continue

    elif option == 2:
        while True:
            try:
                choix_usd = float(input("Entrez un montant en dollars américain : "))
                if choix_usd == 0:
                    break
                elif choix_usd < 0:
                    print("Nombre Incorrect\n")
                    continue

                print(f"{choix_usd} USD = {choix_usd/taux_usd:.2f} EUR\n")
                print("Revenir au menu principal [0]")
            except ValueError:
                print("Nombre incorrect\n")
                continue

    else:
        print("Veuillez entrer une option valide.\n")