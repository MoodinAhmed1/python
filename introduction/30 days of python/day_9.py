#Exercise 1

#Q1
# age = int(input("enter your age: "))
# print("you can drive!") if age >= 18 else print(f"you must wait {18 - age} years to start driving")

#Q2
# my_age = 22
# your_age = int(input("enter your age: "))
# if(your_age > my_age):
#     if(your_age - my_age == 1):
#         print("you're only one year older than me!")
#     else:
#         print(f"you're {your_age - my_age} years older than me!")
# elif(my_age > your_age):
#     if(my_age - your_age == 1):
#         print("i'm only one year older than you")
#     else: 
#         print(f"i'm {my_age - your_age} years older than you!")
# else: 
#     print("we are the same age!")

#Q3
# num_1 = int(input("enter first number: "))
# num_2 = int(input("enter second number: "))
# print(f"{num_1} is greater than {num_2}") if num_1 > num_2 else print(f"{num_1} is less than {num_2}")

#EXERCISE 2
#1 wite code that gives grades based on their scores
# score = int(input("enter your score: "))
# if(score > 80):
#     print("A")
# elif(score > 70): 
#     print("B")
# elif(score > 60):
#     print("C")
# elif(score > 50):
#     print("D")
# else: 
#     print("F")

#2 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# Autumn = ["September", "October", "November"]
# Winter = ["December", "January", "February"]
# Spring = ["March", "April", "May"]
# Summer = ["June", "July", "August"]

# Month = input("what's the current Month? ").title()
# if(Month in Autumn):
#     print(f"{Month} is in the Autumn season")
# elif(Month in Winter):
#     print(f"{Month} is in the Winter season")
# elif(Month in Spring):
#     print(f"{Month} is in the Spring season")
# elif(Month in Summer):
#     print(f"{Month} is in the Summer season")

#3 If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# fruits = ['banana', 'orange', 'mango', 'lemon']
# new_fruit = input("enter fruit: ").lower()
# if(new_fruit in fruits): 
#     print(f"{new_fruit} already exists!")
# else:
#     fruits.append(new_fruit)
#     print(f"new fruits list : {fruits}")

#Exercise 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#1  Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

# if(person['skills']):
#     print(person['skills'][len(person['skills']) // 2])
#     if("Python" in person['skills']):
#         print(f"does python exist? {"Python" in person['skills']}")
    
#2  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# is_frontEnd_developer = "JavaScript" in person['skills'] and "React" in person['skills'] and len(person['skills']) == 2;
# is_backEnd_developer = "Node" in person['skills'] and "Python" in person['skills'] and "MongoDB" in person['skills'] and len(person['skills']) == 3;
# is_full_stack =  "React" in person['skills'] and "Node" in person['skills'] and "MongoDB" in person['skills'];

# if is_frontEnd_developer:
#     print('He is a front end developer')
# elif is_backEnd_developer:
#     print('He is a backend developer')
# elif is_full_stack:
#     print('He is a fullstack developer')
# else:
#     print('He is a nostack developer')