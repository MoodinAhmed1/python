# Find Max in a List

# Write a function that returns the largest number in a list.

# Example: [3, 5, 2, 8, 1] → 8

def max(array):
    max_number_index = 0
    
    for index, num in enumerate(array):
        if num > array[max_number_index]:
            max_number_index = index
    
    return array[max_number_index]

print(max([3, 5, 2, 8, 1]))
    