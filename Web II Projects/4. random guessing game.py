import random

def play():
    secret_number = random.randint(1, 101)
    guess = 0
    
    while True:
        user_input = int(input('enter number between 1 - 100 : '))
        
        if(user_input > secret_number):
            print("too hight")
        
        if(user_input < secret_number):
            print("too low")
        
        if user_input == secret_number:
            print(f"You Won, you guessed it in {guess} times")
        
        guess = guess + 1
        
play();