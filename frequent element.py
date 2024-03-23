#Write a program that finds the most frequent element in a list

from collections import Counter

def most_frequent_element(lst):
    # Count occurrences of each element in the list
    counts = Counter(lst)
    
    # Find the element with the highest count
    most_common = counts.most_common(1)
    
    # Return the most frequent element
    return most_common[0][0] if most_common else None

# Example usage:
my_list = [1, 2, 3, 4, 5, 5, 5, 2, 2, 2, 2, 3, 3]
most_frequent = most_frequent_element(my_list)
print("The most frequent element is:", most_frequent)


#We import the Counter class from the collections module, which allows us to count the occurrences of each element in the list efficiently.
#We define a function most_frequent_element(lst) that takes a list lst as input.
#Inside the function, we create a Counter object called counts to count the occurrences of each element in the list.
#We then use the most_common() method of the Counter object to find the element with the highest count. We specify 1 as the argument to most_common() to get only the most common element.
#Finally, we return the most frequent element. If the list is empty, we return None.

#In the example usage, we create a sample list my_list, call the most_frequent_element() function with this list, and print the result.


