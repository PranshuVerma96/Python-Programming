# .  Describe the way a Python dictionary holds key-value pairs, and explain the basic operations to create, access, modify and remove its entries.

# Dictionary in pyton is a collection of data sotored in key-value pairs Each key is used to access its corresponding value.

# creating the dictionary 
myDict = dict()
print(type(myDict))

# empty dict 
newDict = {}
print(type(newDict))

# creating a dictionary 
studentInfo = {
  "name" : "Dia",
  "age" : 22,
  "course": "BCA",
}

print(studentInfo)

# acccessing value 
print(studentInfo["name"])
# print(studentInfo["Dia"]) # this will rise key error 
# because the dictionary there is no key by name dia

# get method
print(studentInfo.get("name"))

# print(studentInfo.get("dia")) this is occur none instead of 


# modifying value 
studentInfo["age"] = 24
print(studentInfo)

# adding new entries
studentInfo["city"]  = "Lucknow"
print(studentInfo)

# removing Entries 
# python provides several ways to remove dictionay entries
# pop()
# it will return the removed value

removedElement = studentInfo.pop("name")
print(removedElement)

# using clear()
# removes all entries from the dictionary

# studentInfo.clear()
# print(studentInfo)

# using del 
# delete the specified key -value 
del studentInfo["course"]
print(studentInfo)
