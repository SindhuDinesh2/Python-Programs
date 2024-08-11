import random

def generate_specific_random_numbers():
    ranges = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50),
              (51, 60), (61, 70), (71, 80), (81, 90), (91, 100)]
    random_numbers = [random.randint(start, end) for start, end in ranges]
    return random_numbers

print(generate_specific_random_numbers())
