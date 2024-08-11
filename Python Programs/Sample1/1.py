def exchange_numbers(a, b):
    a = a + b  
    b = a - b  
    a = a - b 
    return a, b

a, b = exchange_numbers(2, 3)
print(a, b)
