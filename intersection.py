#Create a program that checks if two sets have any elements in common

def have_common_elements(set1, set2):
    # Check if the intersection of the two sets is not empty
    return len(set1.intersection(set2)) > 0

# Example usage:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
have_common = have_common_elements(set1, set2)
print("Do the sets have any elements in common?", have_common)
