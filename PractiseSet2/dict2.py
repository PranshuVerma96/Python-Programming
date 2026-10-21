# create dict 
from ctypes import c_char


chai_types = {
  "Masala" : "Spicy",
  "Ginger": "Zesty",
  "Green" : "Mild"
}
print(chai_types)
#  access 
print(chai_types["Masala"])
print(chai_types.get("Masalaa"))

#  access and moditfy 
print
chai_types["Green"] = "Ginger"
print(chai_types)

for chai in chai_types:
  print(chai)
  
for key, values,in chai_types.items():
  print(key, values)  
  
if "Msala" in chai_types:
  print("ha he ")

chai_types["Earl Gracy"] = "Chai"

print(chai_types)    

chai_types.pop("Ginger")
print(chai_types)

# # chai_types.popitem("
#                    )