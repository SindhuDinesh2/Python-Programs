def union_lists(list1, list2):
    return list(set(list1) | set(list2))


list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union of lists:", union_lists(list1, list2))
