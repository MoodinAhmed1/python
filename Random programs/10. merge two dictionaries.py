# Write a function that merges two dictionaries. If keys overlap, sum their values.

# Example: {"a": 1, "b": 2} + {"b": 3, "c": 4} → {"a": 1, "b": 5, "c": 4}

def merge(dictionary_1, dictionary_2):
    merged_dictionary = {  }
    
    for item in dictionary_1:
        merged_dictionary[item] = dictionary_1[item]
    
    for item in dictionary_2:
        if item in merged_dictionary:
            merged_dictionary[item] += dictionary_2[item]
        else:
            merged_dictionary[item] = dictionary_2[item]
    
    return merged_dictionary

print(merge( {"a": 1, "b": 2}, {"b": 3, "c": 4}))

