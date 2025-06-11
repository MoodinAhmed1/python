# 5. Word Counter 
# Ask the user to input a sentence or paragraph. 
# Your program should: - Count total words - Count how many times each word appears - Display the most frequent word 
# Use string functions and dictionaries.

def word_counter (sentence) :
    wordCount = {}
    words = sentence.split(" ")
    
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    
    most_frequent_word = sorted(
        wordCount.keys(),
        key = lambda word : wordCount[word],
        reverse = True
    )
    
    most_frequent_word = most_frequent_word[:1]
    
    print("most frequent word is :",most_frequent_word[0], "it has appeared", wordCount[most_frequent_word[0]], "times")

word_counter("Your program should: - Count total words - Count how many times each word appears - Display the most frequent word is usuusalt the word word itself")