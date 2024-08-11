import sys

def sumfile(filename):
    with open(filename, 'r') as file:
        total = sum(int(line.strip()) for line in file)
    return total


if __name__ == "__main__":
    print("Sum:", sumfile('Sample3/numbers.txt'))
