list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find common elements between sets
common_elements = set1.intersection(set2, set3)

# Print the common elements
print("Common elements:", common_elements)
