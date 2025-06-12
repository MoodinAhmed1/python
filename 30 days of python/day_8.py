#Exercise 1
#1 create an empty dictionary called dog
dog = {}

#2 give it keys and values to the dog dictionary
dog["name"] = "bob"
dog['age'] = 7
dog['color'] = "brown-black"
dog['breed'] = "German Shepard"
dog['leg'] = 4

#3 create student dic with the following attribute
student = {
    'first_name' : "mohammed",
    'last_name' : "ahmed",
    'gender' : "M",
    'age' : 22,
    'is_married' : False,
    'skills' : ["JavaScript", "HTML", "CSS", "PHP"],
    'country' : "Ethiopia",
    'city' : "Addis Ababa",
    'address' : {
        'sub_city' : "yeka",
        'wereda' : 2,
        'house_number' : 1572
    }
}

#4 get the length of student directory
print(len(student))

##5 get the type of the skills value
print(type(student['skills']))

#6 modify skills by adding some skills
student['skills'].append("React")
print(student['skills'])

#7 get the dictionary keys as list
keys = student.keys()
print(keys)

#8 get dictionary values as list
values = student.values()
print(values)

#9 get key-value pairs as list of tuples
items = student.items()
print(items)

#10 delete one of the items in the dictionary
del dog['leg']
print(dog)

#11 delete on of the dictionaries
del dog