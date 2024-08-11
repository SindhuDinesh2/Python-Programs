def odd_numbers_in_range(start, end):
    return [i for i in range(start, end + 1) if i % 2 != 0]
print(odd_numbers_in_range(1,100))