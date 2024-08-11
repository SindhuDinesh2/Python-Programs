def concatenate_dicts(dict1, dict2):
    return {**dict1, **dict2}
print("Concatenate Dictionaries:", concatenate_dicts({'a': 1}, {'b': 2}))