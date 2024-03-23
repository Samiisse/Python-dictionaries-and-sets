#Write a program that finds the average value of all the elements in a list of dictionaries

def average_value_of_dicts(list_of_dicts):
    total_sum = 0
    total_count = 0

    # Iterate through each dictionary in the list
    for dictionary in list_of_dicts:
        # Iterate through each value in the dictionary
        for value in dictionary.values():
            # Add the value to the total sum
            total_sum += value
            # Increment the total count
            total_count += 1

    # Calculate the average value
    if total_count == 0:
        return 0  # Avoid division by zero
    else:
        return total_sum / total_count

# Example usage:
list_of_dicts = [{'a': 10, 'b': 20}, {'c': 30, 'd': 40}, {'e': 50, 'f': 60}]
average_value = average_value_of_dicts(list_of_dicts)
print("Average value of all elements:", average_value)
