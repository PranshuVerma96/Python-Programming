#  1.  Describe what Python lists are used for and explain frequently used list operations, namely indexing, slicing, insertion, deletion and sorting.

# list is a iterable in python which has to used for store the different type of data in the contiguos order 

# feature 
# list is followed order
# list is mutable

# syntax 
from ast import If
from encodings.punycode import T
from re import M
import re


myList = [10, 20, "Pranshu",True,'A',20.22]
print(myList)

# access list element
print(myList[5]);

# update list elements 
myList[1] = "Dia"
print(myList)

# add elements append()
myList.append("janvi")
print(myList)

# add mulitple elements extends
myList.extend([10,20,30])
print(myList)
print(myList[8])

# insertElement 
# insert is used for insert the element in postion which is given by the user 

myList.insert(5,"Siya")
print(myList)

# Remove Elements 
# removeElement = myList.remove(10)
# # print(removeElement)
# print(myList)

# Remove the element using pop()
# pop is used for remove the element from the iterable 
# by default it is remove the last element 
# but you can give a specific index also 
# and it will return which element is removed 

removeElement = myList.pop()
print("removed Element :" , removeElement)
print(myList)

# pop using index
removeElement1 = myList.pop(0)
print(removeElement1)
print(myList)

# # Delete Elements using del
# del myList(0)

# clear the list 
# this is method is used for remove the all element form list and return empty list

# myList.clear()
# print(type(myList))
# print(myList)

# find the lenegth 
# this method is used for calculate how maney element are in the list after count the list return the lenght of list 
# print(len(myList))

# sort the list 
# print(myList.sort()) 
# even our list contain different type of data types 
# like string boolean the it will rise a type error because it is not applicable on string boolean ans character 

myMarks = [10,40,20,50,90,30,25]
# print(myMarks.sort()) this is not work with the same type 
# ever you can apply this method like this it will be give none 
myMarks.sort(reverse=True)
# print("Sorted Marks : ", myMarks)

# reverse method 
myList.reverse()
print(myList)

# find the element using index 
firstElement = myList[0]
secondElement = myList[1]

# print(firstElement)
# print(secondElement)

# count occurrences count()
# it is count the occurence and give me the total number of count which is exist in the list 

dataCount = myList.count("Dia")
print(dataCount)

# Check Membership 

if "Dia" in myList:
  print("yes present")
else:
  print("Sorry for that there is noone like diya") 
  
if "Varun" not in myList:
  print("yes you are right") 
else:
  print("sorry there is varun present")
  
# concatnate list using +

data1 = [1,3,4,"Pranshu"]
data2 = [5,6,7,"Dia"]
data3 = data1 + data2
print(data3)
  
# repeat list using *
print(data2 * 3)

# list slicing 
myNewList = [10,20.5,"Dia","Janvi" , True]
print(myList[0]) # it return first element 
# positive slicing 
print(myNewList[1:4])
print(myNewList[0:7])
print(myNewList[0:])
print(myNewList[:1])
print(myNewList[:-1])
print(myNewList[0:-1])
print(myNewList[-5:-1])

# use step 
print(myNewList[1:9 : 2]) 

# Iterate Thorugh a list using for loop
for data in myNewList:
  print(data)

# user input 
# data4 = input("enter data :")
# myNewList.append(data4)
# print(myNewList)

copyList = myNewList.copy()
print("this is myCopy list: " , copyList)

# find the minimum maximum 
# it is not suported all this 
# maxData = max(myNewList)
# print(maxData)

myMarks = [90,78,96,92]
maxMarks = max(myMarks)
print(min(myMarks))
print(maxMarks)

# cacuate the sum 
totatMarks = sum(myMarks)
print(totatMarks)

# nested list 
myNestedList = [10,20,"dia",["ajay",90,"janvi",[40,20]]]
print(myNestedList)
  
  # find element 
print(myList[1]) 
print(myNestedList[1])
print(myNestedList[3][0]) 
print(myNestedList[3][3][0])

# list comprehension 
total = [num**2 for num  in myMarks]
print(total)


myList = [10, 20, 30, 40, 50]

del myList[2]

print(myList)
# # update list item 
# myList[1] = "Dia"
# print(myList)

# # insert the item 
# myList.insert(1 , "Hari")
# print(myList)

# # append() method 
# myList.append(10)
# print(myList)

