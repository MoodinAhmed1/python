# Flatten a Nested List

# Write a function that flattens a nested list into a single list.

# Example: [[1, 2], [3, [4, 5]]] → [1, 2, 3, 4, 5]

def flat(array):
    flattened_list = []
    
    for element in array:
        if type(element) != list:
            flattened_list.append(element)
        else:
            flattened_list.extend(flat(element))
            
    return flattened_list

print(flat([[1, 2], [3, [4, 5]]]))