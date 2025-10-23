import math

D = 0

def calculate_Q_value(D):
    D = float(input("Enter a value from 1 to 10000: "))
    if D not in range(1, 10000+1):
        print("Value error")
        SystemExit
    else :
        Q = math.sqrt((2 * 50 * D) / 30)
        str(Q).split(",")
        return round(Q)

while True:
    choix = input("Enter q to leave or any key to continue: ")

    if choix == "q":
        break
    else:
        print(calculate_Q_value(D))