def create_tuples(nums):
    return [(num, num ** 2) for num in nums]

numbers = [1, 2, 3, 4]
print("List of tuples:", create_tuples(numbers))
