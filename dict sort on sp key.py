#Create a function that takes a list of dictionaries and sorts them based on a specified key

def sort_dicts_by_key(list_of_dicts, key):
    # Sort the list of dictionaries based on the specified key
    sorted_dicts = sorted(list_of_dicts, key=lambda x: x.get(key, float('-inf')))
    return sorted_dicts

# Example usage:
list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]
sorted_list = sort_dicts_by_key(list_of_dicts, 'age')
print("Sorted list of dictionaries:", sorted_list)
