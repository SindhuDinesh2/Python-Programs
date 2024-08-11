def generate_dict(n):
    return {x: (x, x*x, x*x*x) for x in range(1, n+1)}
print("Generate Dictionary:", generate_dict(5))