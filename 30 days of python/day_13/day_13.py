#QUESTION 1
#1 Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
non_positive_numbers = [i for i in numbers if i <= 0]
# print(non_positive_numbers)


#QUESTION 2
# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# for outer_list in list_of_lists: #outer loop
#     for inner_list in outer_list: #inner loop
#         for number in inner_list: #inner inner loop
#             print(number)
flattened_array = [number 
                   for outer_list in list_of_lists #outer loop
                   for inner_list in outer_list #inner loop
                   for number in inner_list #inner inner loop
                   ]
# print(flattened_array)


#QUESTION 3
#Using list comprehension create the following list of tuples: 
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

list_of_tuples = [(i, *[i ** j for j in range(6)]) for i in range(11)]
# for tupples in list_of_tuples:
#     print(tupples)
# #unpacking operator works by unpacking a list that is either inside of list, tupple, function_call, or another unpacking context
# unpack_example = (*[i for i in range(6)],)


#QUESTION 4
#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
flattened_countries = [
    [country[0].upper(), country[0][:3].upper(),country[1].upper()]
    for inner_list in countries
    for country in inner_list
]
# print(flattened_countries)



#QUESTION 5
# Change the following list to a list of dictionaries:
countries = [
    [('Finland', 'Helsinki')], 
    [('Sweden', 'Stockholm')], 
    [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
list_country_dictionaries = [
    {'country' : tupple[0].upper(), 'city' : tupple[1].upper()}
    for row in countries
    for tupple in row
]
# for country in list_country_dictionaries:
#     print(country)




#Question 6
#Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

concatenated_strings = [
    f"{tupple[0]} {tupple[1]}"
    for row in names
    for tupple in row
]
# print(concatenated_strings)



#Question 7]
#Write a lambda function which can solve a slope or y-intercept of linear functions.
