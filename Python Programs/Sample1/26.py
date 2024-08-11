import random

def generate_random_integers(n=20):
    return [random.randint(1, 100) for _ in range(n)]

print(generate_random_integers(20))
