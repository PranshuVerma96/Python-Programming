# 7.  Analyse the choice of functions: (a) contrast a user-defined function with a lambda function for a
# simple calculation; (b) discuss the situations in which an ordinary named function is easier to
# understand than a lambda functio

# function is block of code 
# that is used perfom a specific task 
def Sum(a,b):
  return a+b

result = Sum(10,30)
print(result)

# lambda function 
# this is a anonymous funtion there is not any function name it is the sort version of funtion 
# find the square tof the number 

square = lambda x : x*x
print(square(10))
