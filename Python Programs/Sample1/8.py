def compute_expression(n):
    n_str = str(n)
    return n + int(n_str * 2) + int(n_str * 3)
print(compute_expression(3))