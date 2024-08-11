def unique(lst):
    unique_elements = []
    seen_elements = set()
    
    for item in lst:
        if item not in seen_elements:
            unique_elements.append(item)
            seen_elements.add(item)
    
    return unique_elements


if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
    print("Unique elements:", unique(sample_list))
