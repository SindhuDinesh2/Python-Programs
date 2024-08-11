def remove_key(my_dict, key):
    if key in my_dict:
        del my_dict[key]
    return my_dict
print("Remove Key:", remove_key({'a': 1, 'b': 2, 'c': 3}, 'b'))