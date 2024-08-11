import sys
import shutil

def copyfile(src, dest):
    shutil.copy(src, dest)

if __name__ == "__main__":
    copyfile('Sample3/file.txt', 'Sample3/destination.txt')
