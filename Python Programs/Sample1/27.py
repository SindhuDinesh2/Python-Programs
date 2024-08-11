import random

def generate_unique_random_numbers(n=5, range_start=1, range_end=20):
    return random.sample(range(range_start, range_end + 1), n)

print(generate_unique_random_numbers())
