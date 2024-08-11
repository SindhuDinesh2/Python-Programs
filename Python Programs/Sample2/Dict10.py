def encrypt(phrase, cipher_dict):
    return ''.join(cipher_dict.get(char, char) for char in phrase)

cipher_dict = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', 'h': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'n': 'a', 't': ' ', ' ': 't'}
print("Encrypt using Substitution Cipher:", encrypt("cat", cipher_dict))