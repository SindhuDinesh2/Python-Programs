def dups(lst):
    duplicates = []
    seen_elements = set()
    duplicate_elements = set()
    
    for item in lst:
        if item in seen_elements:
            if item not in duplicate_elements:
                duplicates.append(item)
                duplicate_elements.add(item)
        else:
            seen_elements.add(item)
    
    return duplicates


if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7]
    print("Duplicates:", dups(sample_list))
