def multiply_dict(my_dict):
    result = 1
    for value in my_dict.values():
        result *= value
    return result
print("Multiply Dictionary:", multiply_dict({'a': 2, 'b': 3, 'c': 4}))