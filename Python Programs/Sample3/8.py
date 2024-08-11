import os
import sys

def largest_file(directory):
    largest = None
    largest_size = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            if size > largest_size:
                largest = filename
                largest_size = size
    return largest

if __name__ == "__main__":
    print("Largest file:", largest_file('.'))
