def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit
        n //= 10  
    return total_sum

print(sum_of_digits(1234))
