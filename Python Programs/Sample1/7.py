def smallest_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i
print(smallest_divisor(30))