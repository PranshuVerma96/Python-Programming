# write a program to find out the vowel of the sting 

str = "Pranshu Verma  is abca studnet"
vowel =0
for i in str.lower():
  if i in "aeiou":
    vowel += 1
print("number of vowel in str : " , vowel)    
    