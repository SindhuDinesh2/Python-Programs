import sys

def grep(pattern, filename):
    with open(filename, 'r') as file:
        for line in file:
            if pattern in line:
                print(line, end='')


if __name__ == "__main__":
    grep('Python', 'E:/Python Programs/Sample3/file.txt')
