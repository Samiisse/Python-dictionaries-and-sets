#Given two sets, find the union, intersection, and difference between them

def find_set_operations(set1, set2):
    # Find the union of the two sets
    union_set = set1.union(set2)
    
    # Find the intersection of the two sets
    intersection_set = set1.intersection(set2)
    
    # Find the difference between the two sets (elements in set1 but not in set2)
    difference_set1_set2 = set1.difference(set2)
    
    # Find the difference between the two sets (elements in set2 but not in set1)
    difference_set2_set1 = set2.difference(set1)
    
    return union_set, intersection_set, difference_set1_set2, difference_set2_set1

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union, intersection, difference1_2, difference2_1 = find_set_operations(set1, set2)

print("Union:", union)
print("Intersection:", intersection)
print("Difference (set1 - set2):", difference1_2)
print("Difference (set2 - set1):", difference2_1)
