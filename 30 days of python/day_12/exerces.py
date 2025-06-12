#level 1
#1
# Write a function which generates a six digit/character random_user_id.
# print(random_user_id());
# '1ee33d'
from string import ascii_letters, digits
from random import randint

def random_user_id():
    letters = []
    letters.extend(ascii_letters)
    letters.extend(digits)
    
    user_id_array = []
    
    for i in range(6):
        random_index = randint(0, len(letters) - 1)
        user_id_array.append(letters[random_index])
        
    return "".join(user_id_array)

print(random_user_id())

def random_user_id_2():
    letters = []
    letters.extend(ascii_letters)
    letters.extend(digits)
    
    number_of_char = int(input("enter number of characters for id : "))
    number_of_id = int(input("enter number of id to be generated: "))
    
    all_id = []
    
    for i in range(number_of_id):
        single_id = []
        
        for j in range(number_of_char):
            random_index = randint(0, len(letters) - 1)
            single_id.append(letters[random_index])   
        
        id = "".join(single_id)    
        all_id.append(id)
    
    print("\n".join(all_id))
    
random_user_id_2()

