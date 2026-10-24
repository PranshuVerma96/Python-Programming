# 2.  Analyse list operations: (a) discuss what append(), insert() and extend() do to a list; (b) contrast
# remove(), pop() and del as ways of deleting elements from a list.

myList = [10,20,30,40,50,60]

myList.append(90)
# append insert the element in the last

print(myList)

# extend() this used to insert the multiple elemet in the list at the last 
myList.extend([12,23,24])
print(myList)

# insert in used to insert the at the perticular index which you want 

myList.insert(1,100)
print(myList)

# 2 other remove command 

newList = ["ran",34,45,90,90,"Dia"]
myElement =newList.pop(2)
print(myElement)

# remove  is used to remove the element which you want  but no return 
newList.remove(90)
print(newList)

# del is used to delete is used delte the perticuar element
del newList[0]
print(newList)