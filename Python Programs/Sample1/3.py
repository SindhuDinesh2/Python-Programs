def divisible_numbers_in_range(start, end, divisor):
    return [i for i in range(start, end + 1) if i % divisor == 0]
print(divisible_numbers_in_range(1,100,5))