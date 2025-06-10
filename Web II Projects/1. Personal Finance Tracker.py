#Write a program that allows users to: - Add income and expenses - Show current balance - View transaction history 

transaction_history =  []

current_balance = 0

def add_income(income):
    global current_balance
    current_balance += income  
    transaction_history.append({"income": income})

def add_expense(expense):
    global current_balance
    current_balance -= expense
    transaction_history.append({"expense": expense})

def start_progam():
    while True:
        print("1. Add income")
        print("2. Add expenses")
        print("3. Show current balance")
        print("4. View transaction history")
        print("5. exit")
        
        userInput = input("Enter a number: ")
        
        if userInput == "1":
            income = float(input("Enter income amount: "))
            add_income(income)
            print(f"Income of {income} added.")
        
        elif userInput == "2":
            expense = float(input("Enter expense amount: "))
            add_expense(expense)
            print(f"Expense of {expense} added.")
        
        elif userInput == "3":
            print(f"current balance : {current_balance}")
        
        elif userInput == "4":
            for transaction in transaction_history:
                print(transaction)
        
        elif userInput == "5":
            return
        
        else:
            print("Invalid input. Please enter a number from 1 to 5.")          

start_progam()