#function as parameter

def sum_numbers(nums):
    return sum(nums)

def sumation (function, nums):
    return function(nums)

print(sumation(sum_numbers, [1,2,3]))

#function as a return

def square(x):
    return x * x

def cube(x):
    return x * x * x

def abs(x):
    return x if x > 0 else -(x)

def higher_order_function(type):
    if type.lower() == "square":
        return square
    elif type.lower() == "cube":
        return cube
    elif type.lower() == "abs" or type[:3].lower() == "abs":
        return abs
    else:
        return "invallid option, try square, cube or abs"

result = higher_order_function("square")
print(result(5))
result = higher_order_function("cube")
print(result(5))
result = higher_order_function("abs")
print(result(5))

#Python Closures
#in python we can nest function and closure is just a python term that refers to the ability of the nested function to acess the scope of the enclosing function

#EXAMPLE
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))    

#Python Decorators
#Definetion : it lets us modify a function indirectly
#Example : 
def add(a, b):
    return a + b

def our_decorator(func):
    def wrapper(a,b):
        if a + b < 0:
            a = abs(a)
            b = abs(b)  

        return func(a,b)
    return wrapper

absolute_add = our_decorator(add)

print(absolute_add(-7, 3))

#Example 2
def greetings():
    return "Hello World!"

def to_upper_case(func):
    def wrapper():
        return func().upper()
    return wrapper

result = to_upper_case(greetings)
print(result())

@to_upper_case
def greetings():
    return "Hello World!"
print(greetings())

#Example 3 multiple decorators
def to_upper_case(func):
    def wrapper():
        return func().upper()
    return wrapper

def to_split(function):
    def wrapper():
        func = function()
        split_list = func.split()
        return split_list
    return wrapper

@to_split
@to_upper_case
def greetings():
    return "Hello World!"

print(greetings())

#example 4
#decorators with parametes

def reverse_name(func):
    def wrapper(first_name, last_name):
        first_name, last_name = last_name, first_name
        return func(first_name, last_name)
    return wrapper

def to_title(function):
    def wrapper(first_name, last_name):
        first_name, last_name = first_name.title(), last_name.title()
        return function(first_name, last_name)
    return wrapper

@to_title   
@reverse_name
def greet_non_western(first_name, last_name):
    return f"Hello {first_name} {last_name}"

print(greet_non_western("mohammed", "ahmed"))

#Built-in Higher Order Functions
#Python - Map Function
#the map() function takes a function and an iterator as params
#syntax : map(function, iterator)

#example:
numbers = [1,2,3]

squared_numbers = map(lambda x : x ** 2, numbers)
print(list(squared_numbers))

#Example 2 
string = ["1", "2", "3", "4", "5"]
numbers  = map(lambda x : int(x), string)
print(list(numbers))
