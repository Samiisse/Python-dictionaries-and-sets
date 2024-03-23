#Write a Python program that counts the number of occurrences of each character in a given string using a dictionary

def count_characters(string):
    # Initialize an empty dictionary to store character counts
    char_counts = {}

    # Iterate through each character in the string
    for char in string:
        # Increment the count for the current character in the dictionary
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

# Example usage:
input_string = "hello world"
character_counts = count_characters(input_string)
print("Character counts:", character_counts)
