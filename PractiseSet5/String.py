# 6.  Analyse string handling: (a) discuss how indexing and slicing pull out parts of a string; (b) contrast
# the effects of common string methods used for changing case, splitting and joining

# string is a sequence of character . that is store the data in singele ' ' and double "" and also '''''' 

myString = "A boy who is brave"
# slicing is process to find the sub part of string 
print(myString[0:])
print(myString[0:6])
print(myString[:-1])
print(myString[0::2])
print(myString[::-1])

myNewString = "pransh verma"
print(myNewString.upper())
print(myNewString.lower())
print(myNewString.title())
print(myNewString.capitalize())


# spliting 
ownString = "My name is pranshu"
myList = []
myList=  ownString.split(" ")
print(myList)

myNewList = ["a","boay ","is ", "man"]

mySrtingData = "".join(myNewList)
print(mySrtingData)