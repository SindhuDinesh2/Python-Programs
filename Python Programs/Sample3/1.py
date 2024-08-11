import sys

def cat(filename):
    with open(filename, 'r') as file:
        print(file.read())


if __name__ == "__main__":
    cat('e:/Python Programs/Sample3/file.txt')
