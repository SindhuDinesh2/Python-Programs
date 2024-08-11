import os
import sys

def ls(path='.'):
    for filename in os.listdir(path):
        print(filename)


if __name__ == "__main__":
    ls('.')
