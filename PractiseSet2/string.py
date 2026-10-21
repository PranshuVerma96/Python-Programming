# Q. Describe what a Python string is and explain the basic operations used to create, access, modify, search, and manipulate strings.

# string is a sequence of character 
# sequnce of character 
# every character has a position 
# string use single double and tripe quotes 

# create a sting
from operator import concat, le
from re import M
import re
from tkinter import N
from turtle import st


myStr = "Pranshu Verma"

# access character 
print(myStr[0])

# String slicing 
print(myStr[0:])
print(myStr[:])
print(myStr[0:8])
print(myStr[:9])
print(myStr[0:9:2])
# print(myStr[::-1])

# revere the string 
myNewStr = "Dia sharma"
# print(myNewStr[::-1])

# concatenation of string 
str1 = "Pranshu"
str2 = "Mohan"
str3 = str1 + str2
print(str3)

new = concat(str1,str2)
print(new)

# string Repetion 
print(myNewStr*3)

# find the len
lenth = len(myNewStr)
print(lenth)

# check membership 
myNewString = "a boy has a mind"
output = "o" in myNewString
# print(output)

output2 = "z" not in myNewString
# print(output2)

# string immutability 
# myNewString[0] = "B" # it will occur error
# # print(myNewString) 

# # convert to uppercase 
# myNewString.upper()
# print(myNewString)
# newAtrer = myNewString.upper()
# print(newAtrer)

# # conver to lower case 
# newAterLower = myNewString.lower()
# # print(newAterLower)

# capitalize a string 
# stringWithCap = myNewString.capitalize()
# print(stringWithCap)

# # conver the title case 
# strWithTit = myNewString.title()
# print(strWithTit)

# find  a string 
findStr = myNewString.find("boy")
print(findStr)

# count occurance 
countStr = myNewString.count("a")
print(countStr)

# replace a sub string
# replaceWith = myNewString.replace("boy","Girl")
# print(replaceWith)

# split a string 

# newList = myNewString.split(" ")
# print(newList)

# join string 
joinStr = ["a" , "man","who" , "name" , "is" , "mohit"]
newStr = " ".join(joinStr)
print(newStr)

# remove whitespace 
myName = "   Pranshu Verma"
print(myName)
removeSpcae = myName.strip()
print(removeSpcae)

# check string content isalpha isdigit isalnum
myNewDate = "pranshuA"
print(myNewDate.isalnum())
print(myNewDate.isdigit())
print(myNewDate.isalpha())

# check prefix ans suffix 
print(myNewDate.startswith("p"))
print(myNewDate.endswith("o"))

# sting formatting 
name = "pranshu"
myNewString = "A day is a beautiful day {}"
myNewString= myNewString.format(name)

print(myNewString)


# sting comparison 
strA = "Pranshu"
strB = "Gia"
print(strA == strB)
print(strA != strB)

newA = "pranshu"
for ch in newA:
  print(ch)


  