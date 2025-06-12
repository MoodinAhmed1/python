#LAMBDA FUNCTION
#Lambda dunction is a small anonymous function that can take any number of parameters but only have one expression

#to create a lambda function we use the lambda key word followed by parameter(s) : followed by an expression
#Syntax: x = lambda param1, param2, param3 : param1 + param2 + param3
#example: add_two_numx = lambda x, y : x + y

#self invocking lambda :
# (lambda x , y : x + y)(5,3)

#lambda inside another function
#def power(x):
    #return lambda n : x ** n
#print(power(2)(3))
#what happened here is that the power(2) returned lambda n : 2 ** n, therefor we pass 3 alongside power(3)(2) as n and we get the expression 2 ** 3 which evaluates to 8 and then we print it all as print(power(2)(3))