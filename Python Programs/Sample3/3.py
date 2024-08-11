import sys

def head(filename, n=5):
    with open(filename, 'r') as file:
        for _ in range(n):
            line = file.readline()
            if line:
                print(line, end='')
            else:
                break


if __name__ == "__main__":
    head('e:/Python Programs/Sample3/file.txt')
