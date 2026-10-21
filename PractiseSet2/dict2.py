# # create dict 
# from ctypes import c_char


# chai_types = {
#   "Masala" : "Spicy",
#   "Ginger": "Zesty",
#   "Green" : "Mild"
# }
# print(chai_types)
# #  access 
# print(chai_types["Masala"])
# print(chai_types.get("Masalaa"))

# #  access and moditfy 
# print
# chai_types["Green"] = "Ginger"
# print(chai_types)

# for chai in chai_types:
#   print(chai)
  
# for key, values,in chai_types.items():
#   print(key, values)  
  
# if "Msala" in chai_types:
#   print("ha he ")

# chai_types["Earl Gracy"] = "Chai"

# print(chai_types)    

# chai_types.pop("Ginger")
# print(chai_types)

# # # chai_types.popitem("
# #          
# )

# 4.  Describe the way a Python dictionary holds key-value pairs, and explain the basic operations to
# create, access, modify and remove its entries.

# create a dictionary
from encodings.punycode import T
from operator import le, mul
import re


myDict = {
  "name" : "Dia",
  "marks":90,
  "age" : 21
}

# accesselement
# print(myDict["name"])
dataValue = myDict["name"]
print(dataValue)

# using get key method 
# retrieves a value safely returns none if the key is missing by default

dataValue2= myDict.get("name")
dataValue2= myDict.get("name1")  # this will give none becacuse there is no key as name1

print(dataValue2)

# add adds a new value pair
myDict["city"] = "Lucknow"
print(myDict)

# update modifies an existing value
myDict["city"] = "Noida"
print(myDict)

# update using update method adds new entries or updates existing entries
# this is method is used to update the existing the value other the value is not existing thean it will insert the value 

myDict.update({"game":23}) 
print(myDict)

# Remove item
removedItem = myDict.pop("game")
print(removedItem)
print(myDict)

# using remove popitem()
# removes a specified key and returns its value
# removedStop = myDict.popitem()
# print(type(removedStop))
# print(removedStop)

# remove using del : Deletes a specified key value pair
# del myDict["name"]
# print(myDict)

# clear : removes all key value pairs
# myDict.clear()
# print(myDict)

# get all values using 
# allkeys = myDict.keys()
# print(type(allkeys))
# print(allkeys)

# get all value 
# returns all values
allkeys = myDict.keys()
# print(allkeys)

# get all items using items 
allitems = myDict.items()
# print(type(allitems))
# print(allitems)

# Check membership
value = "name" in myDict
# print(value)

# check value is not presnt
valueNot = "gf" not in myDict
# print(valueNot) 

# copy using copy create a shallow copy of the dictionary

# myNewDict = dict() this will give error this is not valid syntex
# myDict.copy(myNewDict)
# print(myNewDict)

myNewDict = myDict.copy()
print(myNewDict)

myNewDict["name"] = "siya"
print(myNewDict)
print(myDict)

# create the dictionary using dict constructor
# myNewestDict = dict({
#   "name" : "rahul",
#   "marks":90
# })
# print(myNewestDict)

# del myDict
# print(myDict)

# iterate through keys loops through the dictionary 
for key in myDict:
  print(key)

# iterate through values 
for values in myDict:
  print(values)
  
# iterate through items  # 
for key,value in myDict.items():
  print("key : ",key ,"  ", "value : ",value )
  
myLength = len(myDict)  
print(myLength)
   

student = {
    "name": "Pranshu",
    "age": 21
}

result = student.setdefault("name", "Rahul")
result = student.setdefault("city","Lucknow")

print(result)
print(student)