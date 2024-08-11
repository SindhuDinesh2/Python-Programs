def count_digits_and_letters(s):
    digit_count = sum(1 for char in s if char.isdigit())
    letter_count = sum(1 for char in s if char.isalpha())
    return digit_count, letter_count
print(count_digits_and_letters("My phone number is 98765"))