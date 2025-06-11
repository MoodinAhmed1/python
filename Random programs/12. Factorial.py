# 10. Factorial of a Number
# - Write a function that computes the factorial of a number (using loops or recursion).
# - Example: 5! → 120

def fact(num):
    
    factorial = 1
    
    if num == 1:
        return 1
    
    factorial = num * fact(num - 1)
    
    return factorial

print("5! ->",fact(5))

