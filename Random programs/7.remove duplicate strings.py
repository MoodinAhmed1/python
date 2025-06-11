# Remove Duplicates from a String

# Write a function that removes duplicate characters from a string.

# Example: "programming" → "progamin"

def remove_dup(word):
    new_word = []
    
    for letter in word:
        if letter not in new_word:
            new_word.append(letter)
    
    new_word = "".join(new_word)
    return new_word

print(remove_dup("hello"))