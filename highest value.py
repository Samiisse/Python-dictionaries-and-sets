#Given a list of dictionaries, find the dictionary with the highest value for a specific key

def find_dict_with_highest_value(dicts, key):
    # Use the max function with a custom key function to find the dictionary with the highest value for the specified key
    return max(dicts, key=lambda x: x.get(key, float('-inf')))

# Example usage:
list_of_dicts = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 5, 'b': 6}]
highest_value_dict = find_dict_with_highest_value(list_of_dicts, 'a')
print("Dictionary with the highest value for key 'a':", highest_value_dict)
