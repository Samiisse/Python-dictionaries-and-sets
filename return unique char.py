#Implement a function that takes a list of strings and returns a set of unique characters present in all strings.

def unique_characters_in_all_strings(string_list):
    # Initialize a set with all characters from the first string
    unique_chars = set(string_list[0])

    # Iterate through the remaining strings
    for string in string_list[1:]:
        # Update the set to contain only characters present in both sets
        unique_chars &= set(string)

    return unique_chars

# Example usage:
strings = ["hello", "world", "python"]
unique_chars = unique_characters_in_all_strings(strings)
print("Unique characters present in all strings:", unique_chars)
