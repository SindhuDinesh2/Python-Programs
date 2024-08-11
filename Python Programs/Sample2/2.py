def find_second_largest(nums):
    first, second = float('-inf'), float('-inf')
    for num in nums:
        if num > first:
            first, second = num, first
        elif first > num > second:
            second = num
    return second


numbers = [1,3,7,4,0]
print("Second largest number:", find_second_largest(numbers))
