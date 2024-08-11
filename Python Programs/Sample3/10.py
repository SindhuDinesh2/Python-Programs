import os
import sys

def files_only(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

if __name__ == "__main__":
    print("Files only:", files_only('.'))
