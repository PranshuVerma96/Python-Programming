# 6.  Analyse functions and modules: (a) distinguish between a user-defined function and a lambda
# function; (b) discuss why the Math module is imported and how its functions are used; (c) write a
# program that defines a function to square a number and also makes use of a suitable Math
# module function.

# lambda function is a anonymous function that can take any number of argument but contain only one expression 

squre = lambda x : x*x
print(squre(5))

# why useful 
# shorter code 
# used for simple calculation
# useful when a fuction is needed only for short time

# module is a python file that contains code such as function classes and variables which can be reused in another python program

import math
import random

print(math.sqrt(4545))
print(math.ceil(9.33))
print(math.floor(9.33))
print(math.pi)
print(math.factorial(9))

print(random.random())
