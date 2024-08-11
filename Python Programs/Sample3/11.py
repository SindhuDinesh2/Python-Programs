import os
import sys
import fnmatch

def find_matching_files(directory, pattern):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            matching_files.append(os.path.join(root, filename))
    return matching_files


if __name__ == "__main__":
    matches = find_matching_files('.', '*.txt')
    for match in matches:
        print(match)
