import random

def generate_even_numbers():
    numbers = [i for i in range(150, 251)]
    even = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)
    return random.sample(even, 5)
    

print(generate_even_numbers())