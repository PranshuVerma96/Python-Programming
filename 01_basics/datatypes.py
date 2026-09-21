# data types in python 
# object types / data types

# Numbers  1234 ,3.123,4+4j, 0nill, Decimal 
# decimal 
# string 

# list ek continues memory location 
# mylist = [1,2,3,4,[]]
# #Tuple : (1,2,3,"pranshu") 
# [], (),{}

# dictionary : {'food' : 'spam'}
# Set () , {'a','b','c'}

# File :opem('ex.text'),open(r....)

# Boolean : true, false,
# None : None
# Functions , modules, classes, instnces, 
# advance Decorator , Generators, Iterators, meta programming

a = 13
b = 13
sum  = a+b
print(sum)

# find power 
x = 2
result = x**x
print(result)

# we can import things 
import math
from re import L, U
print(math.pi)

import random
print(random.random())

print(random.choice([1,2,3,4]))

# string 
username = "chai aur code"
print(len(username))

print(username[1])

# username[0] = "p"
# print(username[0])
# if we can try to manipulate in string it will be occur a error
# TypeError: 'str' object does not support item assignment

print(username[-1])

print(username[1:5])

# print(dir(username))

# list 
myList = [123,"chai", 3.14,]
print(len(myList))
print(myList[0])

# dictionary 
mydict = {
  'one' : 'lemaon tea',
  'two' : 'ginger',
  'there' : 'superman',
  'hero' : 'thor'
}

print(mydict)
print(mydict['one'])

# Tuples
myTup = (1,2,3,4)
print(myTup)
print(len(myTup))