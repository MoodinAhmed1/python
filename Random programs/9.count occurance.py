# Count Occurrences in a List

# Write a function that counts how many times each item appears in a list.

# Example: ["apple", "banana", "apple", "orange"] → {"apple": 2, "banana": 1, "orange": 1}

def count(array):
    count = {}
    for item in array:
        if item in count:
            count[item] += 1
        else : 
            count[item] = 1

    return count

print(count(["apple", "banana", "apple", "orange"]))
