#Given two dictionaries, merge them into a single dictionary

# Two dictionaries to merge
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge the dictionaries using dictionary unpacking
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print(merged_dict)
