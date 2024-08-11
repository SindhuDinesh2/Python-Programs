import sys

def wc(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
    return line_count, word_count, char_count

if __name__ == "__main__":
    lines, words, chars = wc('e:/Python Programs/Sample3/file.txt')
    print(f"Lines: {lines}, Words: {words}, Characters: {chars}")
