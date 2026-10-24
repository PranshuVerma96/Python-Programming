# .  Analyse set operations in Python: (a) contrast union, intersection and difference using two simple
# sets; (b) discuss how a set can eliminate duplicate values from a collection and justify why it is
# suitable.

# set is data type  in python and this is most useful where we need to data soret uniquely we must used set 
# becase it do not coantin duplcate bale 
# you can not find element using index 
# there you can not insert at the any specific postion 

set = {10,20,30,40,"Priya"}
print(set)

set.add(40)
print(set)

# union this is a operation here we can find the combine two set and write the duplicate elemen one 
setA = {10,30,40,50}
setB = {50,55,60,80}

setC = setA.union(setB)
print(setC)

# intersecion 
setD = setA.intersection(setB)
print(setD)

# difference 

setE = setA.difference(setB)
print(setE)

# symetric differene

setF = setA.symmetric_difference(setB)
