# 2.  Distinguish between a list and a tuple in terms of mutability, element access and appropriate situations for using each.

# List is iterator in which we can access add delete element
# tuple is a iterator in which we can not mutate it is also used to store data.

# tuble is an ordered and immutable collection used to store multiple elements of different data types. Once a tuple is created its elements cannot be added, removed, or modified directly.

# creating a tuple
from operator import le


mytuple = ()
print(type(mytuple))

newTuple = tuple()
print(type(newTuple))

nextTuple = 19,29,30
print(type(nextTuple))

tea_types = ("Black" , "Green", "Oolong" )
print(tea_types)

print(tea_types[0])

# tea_types[0] = "white"
print(tea_types) # this will rise a error 
# tuple object does not supprot item assignment

print(len(tea_types))

more_tea = ("herbal", "Earl Grey")

# concate both tuple 
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
  print("I have green tea")
  
more_tea = ("herbal","herbal","gray")
print(more_tea.count("herbal"))  
print(len(more_tea))

# ("herbal", "Earl Grey")
# ("herbal", "Earl Grey") = tea_types

print("herbal")
