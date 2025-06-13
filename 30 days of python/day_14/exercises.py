countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Question 1
# What is the difference between map, filter and reduce?
# the difference between map, filter and reduce is that 
# - map applies the funtion to all elemnts if the list and returns a new list, 
# - filer, as it's name indicate filters the elemts that return true to the function given and returns a new list
# - reduce takes a function and iteratable aswell but doesnt return a list, instead applies the function to all elements and returns a single value

# Question 2 
# explain the difference between higher order function , closer and decorator
# higher order functions are functions that take functions as parameter, or return a fucntion from a functions
# closure is just a function defined in another fuunctions thus access all the variables of the enclosed functions(parent function)
# decorators are functions that take other functions as parameters alters their behaviour and returns the altered function without affecting the original functions

# Question 3
# Define a call function before map, filter or reduce, see examples.
from functools import reduce

def double(x):
    return x * 2

def even(x):
    return True if x % 2 == 0 else False

def add_numbers(x,y):
    return x + y

doubled_numbers = list(map(double, numbers))
even_numbers = list(filter(even, numbers))
numbers_multiplied = reduce(add_numbers, numbers)

print(doubled_numbers)
print(even_numbers)
print(numbers_multiplied)

# Question 4
# Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# Question 5
# Use for to print each name in the names list.
for name in names:
    print (name)


# Question 6
# Use for to print each number in the numbers list.
for number in numbers:
    print(number)

# EXERCISE 2
# Question 1
# Use map to create a new list by changing each country to uppercase in the countries list
upcase_countries = list(map(lambda country: country.upper(), countries))
print(upcase_countries)

# Question 2
# Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(lambda x : x ** 2, numbers))
print(squared_numbers)

# Question 3
# Use map to change each name to uppercase in the names list
upcase_names = list(map(lambda name: name.upper(), names))
print(upcase_names)

# Question 4 
# Use filter to filter out countries containing 'land'.
land_countries = list(filter(lambda x : x.lower().endswith('land'), countries))
print(land_countries)

# Question 5
# Use filter to filter out countries having exactly six characters.
six_letter_countries = list(filter(lambda country : len(country) == 6, countries))
print(six_letter_countries)

# Question 6
# Use filter to filter out countries containing six letters and more in the country list.
six_letter_or_more_countries = list(filter(lambda country : len(country) >= 6, countries))
print(six_letter_or_more_countries)

# Question 7
# Use filter to filter out countries starting with an 'E'
filtered_e_countries = list(filter(lambda country : not country.startswith("E"), countries))
print(filtered_e_countries)


# Question 8
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
chained = reduce(add_numbers, filter(even, map(double, numbers)))
print(chained)

# Question 9
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(array):
    return list(filter(lambda item : type(item) == "str", array))

# Question 10
# Use reduce to sum all the numbers in the numbers list.
sum = reduce(lambda x , y : x + y, numbers)
print(sum)

# Question 11
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
sentence = reduce(lambda x , y :f"{x}, {y}", countries[:-1]) + f" and {countries[-1]} are north European countries"
print(sentence)

# Question 12 
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries_list import countries
patterns = ['land', 'ia', 'stan', 'new']

def categorize():
    categories = {}
    for pattern in patterns :
        categories[pattern] = []

    for country in countries:
        if country.endswith(patterns[0]):
            categories[patterns[0]].append(country)
        elif country.endswith(patterns[1]):
            categories[patterns[1]].append(country)
        elif country.endswith(patterns[2]):
            categories[patterns[2]].append(country)
        elif country.startswith(patterns[3]):
            categories[patterns[3]].append(country)
        
    return categories

result = categorize()

for pattern, countires in result.items():
    print(f"{pattern} : {countires}\n")

