# Unpacking lists       
array = [1,2,3]
def sum_all(*args):
    s = 0
    for number in args:
        s += number
    return s

print(sum_all(*array))

# Unpacking Dictionaries
person = {"name" : "moahhmed", "age" : 20}

def print_info(**kwargs):
    for key in kwargs:
        print(kwargs[key])

print_info(**person)

# Packing Dictionaries
def define_object(**kwargs):
    return kwargs
    
me = define_object(name = "mohammed", age = 22)

print(me)

# Speading in python
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [0, *lst1, *lst2]
print(lst3)

# Enumerate :- if we are intrested in the index of each element and the element in a list we can use enumerate built-in function
for index, element in enumerate([1,2,3]):
    print(index , element)

# Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veggies = []
for f , v in zip(fruits, vegetables):
    fruits_and_veggies.append({'fruit': f, "veggies" : v})

print(fruits_and_veggies)

# Exercise
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
# 🎉 CONGRATULATIONS ! 🎉

*nordic_countries, es, ru = names
print(nordic_countries, es, ru)

