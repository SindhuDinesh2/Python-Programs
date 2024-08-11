def find_longest_word(words):
    return max(words, key=len)


words = ["siri","hari","isha","ishan"]
print("Longest word:", find_longest_word(words))
