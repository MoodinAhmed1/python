#importing the whole module
import my_module
name = my_module.generate_full_name("amir", "mohammed")
print(name)

#importing specific fucntions of a module and renaming them
from my_module import generate_full_name as full_name, person as p
name = full_name("sultan", "mohammed")
f_name, l_name = name.split(" ")
my_child = p(f_name, l_name)
print(my_child["first_name"])


#importing OS mosule that can interact with files and irectories, create, delete rename, move, copy etc... files and directories
import os
new_file = os.mkdir("my new python.py")
os.rmdir("my new python.py")
print(os.getcwd())

#importing SYS module
import sys
print(sys.path[0])

#importing everything from the statistics modulude that provides statistically functions
from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

#importing math module
import math
print(math.pi)
print(math.pow(2, 3))
print(math.ceil(2.33))
print(math.factorial(5))

#importing string modules which can provide us all the alphabets, numbers and symbols
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#importing random module that has 2 most important functions like random() and randint()
import random
print(random.random()) #random() takes no argument and generates a random number between 0-0.999
print(random.randint(0,10)) #randint(start, end) takes two arguments and returns a random value in range of the given argument (inclusive)

random_count = {}
for i in range(1000):
    randomNumber = random.randint(0,10)
    
    if randomNumber in random_count:
        random_count[randomNumber] += 1
    else:
        random_count[randomNumber] = 1
        
random_count = sorted(
    random_count.items(),
    key = lambda item : item[1],
    reverse = True
)

print(random_count)