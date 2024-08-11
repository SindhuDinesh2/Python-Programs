import os
import sys

def most_recent_file(directory):
    most_recent = None
    most_recent_time = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_time = os.path.getmtime(filepath)
            if file_time > most_recent_time:
                most_recent = filename
                most_recent_time = file_time
    return most_recent


if __name__ == "__main__":
    print("Most recent file:", most_recent_file('.'))
