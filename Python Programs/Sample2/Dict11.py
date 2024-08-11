import random

def make_cipher_dict(alphabet):
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))
print("Generate Cipher Dictionary:", make_cipher_dict("abcdefghijklmnopqrstuvwxyz"))