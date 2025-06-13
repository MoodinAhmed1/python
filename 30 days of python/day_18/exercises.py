import string
import re

# EXERCISE 1
# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\b\w+\b', paragraph)
unique_words = set(words)

word_counter = []
for word in unique_words:
    match = re.findall(rf'\b{re.escape(word)}\b', paragraph)
    word_counter.append((len(match), word))

word_counter.sort(reverse=True)


for count in word_counter:
    print(count)

# Question 2
# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
# points = ['-12', '-4', '-3', '-1', '0', '4', '8']
# sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 -(-12) # 20
txt = 'he position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
points = re.findall(r'-?\d+', txt)
points = [int(point) for point in points]
sorted_points = sorted(points)
distance = sorted_points[-1] - sorted_points[0]
print(distance)

# Exercises: Level 2
# 1. Write a pattern which identifies if a string is a valid python variable
# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

def is_valid (variable):
    not_valid_patters = []
    not_valid_patters.append('^[0-9]')
    not_valid_patters.append('-.+')
    not_valid_patters.extend([f'^{re.escape(symbol)}' for symbol in string.punctuation])

    for pattern in not_valid_patters:
        if re.search(pattern, variable):
            return False
    return True

print(is_valid('first_name')) # True
print(is_valid('first-name')) # False
print(is_valid('1first_name')) # False
print(is_valid('firstname')) # True

# Exercises: Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
# print(clean_text(sentence));
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
def clean_text(sentence):
    clean_text = re.sub("[$]", "", sentence)
    clean_text = re.sub("[%]", "", clean_text)
    clean_text = re.sub("[@]", "", clean_text)
    clean_text = re.sub("[;]", "", clean_text)
    clean_text = re.sub("[&]", "", clean_text)
    clean_text = re.sub("[#]", "", clean_text)

    return clean_text

cleaned_text = clean_text(sentence)

def most_frequent_words(sentence):
    count = []
    words = re.findall(r'\b\w+\b', sentence)
    words = set(words)

    for word in words:
        match = re.findall(rf"\b{word}\b", sentence)
        count.append((len(match), word))

    count.sort(reverse=True)

    return count

print(cleaned_text)
for index, count in enumerate(most_frequent_words(cleaned_text)):
    if(index == 3):
        break

    print(count)
