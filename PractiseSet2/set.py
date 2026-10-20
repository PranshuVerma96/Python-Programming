# 3.  Explain what a Python set is and describe the use of typical set operations like union, intersection and difference.

# a set in python is an unordered collection of unique elements. it does not allow duplicate element. set are mutable, which means we can add or remove elements after creating a set. 

# Features of set
# Sets store unique elements 
# Set are unordered collection 
# sets do nor support indexing or slicing#

mySet = {}
print(type(mySet)) # it will return the dictionary 

mySet = {10,30,40,50,90}
print(mySet)

# union oeration combines all unique elemnt from two sets.
setA = {10,30,40,50}
setB = {60,30,70,70,90}
finalSet = setA.union(setB)

print(finalSet)

# intersection operation  this operation returns only the elements that are common to both sets
# anotherSet = setA.intersection(setB)
anotherSet = setA & setB
print(anotherSet)

# Difference operation 
# the difference operation returns the elements that are present in the first set but not in the second set
diffSet = setA.difference(setB)
print(diffSet)

# other common set operations 
# add an element 
my_set = {10,30,"diaya"}
my_set.add("Siya")
print(type(my_set))
print(my_set)

# remove an elements 
my_set.remove(10)
print(my_set)

# check membership 
# the in operator checks whether an elements exists in a set

myNewSet = {10,30,40,"diay","Siya",True}
print(20 in myNewSet)

# Symmetric Diffierence 
newSetA = {10,20,30,40,50}
newSetB = {10,80,90,20,40}

new_MadeSet = newSetA.symmetric_difference(newSetB)
print(new_MadeSet)