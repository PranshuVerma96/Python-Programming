# List maney community know as array

from hmac import new
from re import S


tea_varities = ["Black","Green" , "Oolong","White"]
print(tea_varities)

# find random elemnt
print(tea_varities[0])

# find the last element
print(tea_varities[-1])

# slicing
print(tea_varities[:2])

# update the list
tea_varities[3] = "Herbal"
print(tea_varities)

#  sting treat as array
# tea_varities[1:2] = "Lemon"
# print(tea_varities)

# if you want to update value as a slicint
tea_varities[1:2] = ["BlackGold"]
print(tea_varities)

# here 
tea_varities[1] = "Lemon"
print(tea_varities)

# slicing
print(tea_varities[1:3])

tea_varities[1:3] = ["Green", "Masala"]
print(tea_varities)

print(tea_varities[1:1]) # it return empty array

tea_varities[1:1] = ["test","test"]
print(tea_varities)

print(tea_varities[1:2])

tea_varities[1:3]= []
print(tea_varities)

# how to iterate in list

# for tea in tea_varities:
  # print(tea)
  # print(tea , end="-")

  #  kush nahi raega
  #  append method
tea_varities.append("Oolong")  
if "Oolong" in tea_varities:
  print("I have Oolong tea")  

  # pop method 
  print(tea_varities.pop())
  print(tea_varities) 
  
  # remove method  
tea_varities.remove("Black")
print(tea_varities)  

# Insert in list 
tea_varities.insert(3,"Green")
print(tea_varities)

# tea_varities_copy = tea_varities

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)

tea_varities_copy.append("LemonTea")
print(tea_varities)
print(tea_varities_copy)

#  list compenstion 
y = print(range(10))

# print(y)

# it return a squred nums to the given matrix
squared_nums = [x**2 for x in range(10)]
print(squared_nums)

quarard_nums = [x**3 for x in range(20)]
print(quarard_nums)

# find the length
print(len(quarard_nums))

# find the sum 
sum = sum(quarard_nums)
print(sum)

print(quarard_nums.pop(3))
print(quarard_nums)

# reverse of list
nums = [10,30,23,55,26,7,8]
nums.reverse()
print(nums)

# sort 
# nums.sort()
# print(nums)  

# find the index 
print(nums.index(30))

# expend add multiple element in the list 
nums.extend([1,2,3,4])
print(nums)

# count 
print(nums.count(10))

# clear method
nums.clear()
print(nums)

