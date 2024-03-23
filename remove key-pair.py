#Implement a function that removes a key-value pair from a dictionary

def remove_key_value_pair(dictionary, key):
    # Check if the key exists in the dictionary
    if key in dictionary:
        # Remove the key-value pair and return the value
        return dictionary.pop(key)
    else:
        # Key does not exist, return None or raise an error
        return None  # or raise KeyError("Key not found")

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_value = remove_key_value_pair(my_dict, 'b')
print("Removed value:", removed_value)
print("Dictionary after removal:", my_dict)
