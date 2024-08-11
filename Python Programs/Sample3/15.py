def group(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    size = 3
    print("Grouped lists:", group(sample_list, size))
