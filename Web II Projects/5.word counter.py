# 5. Word Counter 
# Ask the user to input a sentence or paragraph. 
# Your program should: - Count total words - Count how many times each word appears - Display the most frequent word 
# Use string functions and dictionaries.

def word_counter(sentence) :
    words = sentence.split(" ")
    length = len(words)
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    most_frequent_word = sorted(
        word_count.keys(),
        key= lambda word: word_count[word],
        reverse=True
    )
    
    most_frequent_word = most_frequent_word[0:1]
    
    print(f"total words: {length}")
    print(f"most frequent word is {most_frequent_word[0]} and it had apeared {word_count[most_frequent_word[0]]} times")

word_counter("hello i'm mohammed and i'm the happiest mohammed ever mohammed")