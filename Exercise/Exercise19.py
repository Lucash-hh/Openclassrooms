import random

def generate_random_numbers():
    numbers = [i for i in range(150, 251)]
    return random.sample(numbers, 5)


print(generate_random_numbers())
