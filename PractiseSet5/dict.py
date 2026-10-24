# 3.  Analyse how dictionaries are used: (a) discuss the way keys and values are created, accessed
# and modified in a dictionary holding student records; (b) contrast a dictionary with a list for
# storing the named attributes of a student.

# dictionary is data type in python which is used to store the data in key value pair form 

myDict = {
  "name" :  "Pranshu",
  "Age":18,
  "Salary": 40000,
  "Role":"Software engineer"
}

print(myDict)
# accessed the value of dictionary 
# this is if value is not present it will occur error
value = myDict["name"]
print(value)

# we have access the elemet using get method 
# it will none if value is not present 
ageData = myDict.get("Age")
print(ageData)

myDict["name"] =  "Dia"
myDict["role"] = "AI Engineer"
print(myDict)

newDict = {
  "name" : "Riya Sharma",
  "Marks" : [96,92,92,92,70]
}

print(newDict)