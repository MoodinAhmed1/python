# Fibonacci Sequence

# Write a function that generates the first n Fibonacci numbers.

# Example: n = 5 → [0, 1, 1, 2, 3]

def fib(n):
    num1 = 0
    num2 = 1
    
    Fibonacci_sequence = []
    
    for i in range(n):
        Fibonacci_sequence.append(num1)
        
        sum = num1 + num2
        num1 = num2
        num2 = sum
        
        
    return Fibonacci_sequence

print(fib(5))