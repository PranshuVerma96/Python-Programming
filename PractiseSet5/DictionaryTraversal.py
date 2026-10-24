# 11.  Analyse traversal: (a) contrast looping over a string with looping over a dictionary using a for
# loop; (b) discuss the cases where a while loop suits repeated input better than a for loop

# traversal on string 
myStr = "Pranshu Verma"

# for i in myStr:
  # print(i)

myDict = {
  "name" : "Dia",
  "Age": 34,
  "Salary":344,
  "Role" : "Engineer"
}

# find the vowel 
vowel = 0
for i in myStr:
  if( i in "aeiou"):
    vowel +=1

print(vowel)    

# traverse on dictionary only value 

for value in myDict.values():
  print(value)
  
  #  find the key 
  
for key in myDict.keys():
  print(key) 
   
for key, value in myDict.items():
  print("keys " , key , " " , "Values : ", value)   