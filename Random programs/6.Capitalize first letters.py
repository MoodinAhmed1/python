# 4. Capitalize First Letters

# Write a function that capitalizes the first letter of each word in a sentence.

# Example: "hello world" → "Hello World"

def capitalize_first_letter(sentence):
    words = sentence.split(" ")
    for index, word in enumerate(words):
        first_letter = word[0].upper()
        
        words[index] = f"{first_letter}{word[1:]}"
        
    words = " ".join(words)
    
    print(words)

capitalize_first_letter("Write a function that capitalizes the first letter of each word in a sentence.")