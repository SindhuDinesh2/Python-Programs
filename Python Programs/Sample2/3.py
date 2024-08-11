def split_even_odd(nums):
    even = [num for num in nums if num % 2 == 0]
    odd = [num for num in nums if num % 2 != 0]
    return even, odd


numbers = [1,9,2,8,3,7,4,6]
even_list, odd_list = split_even_odd(numbers)
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
