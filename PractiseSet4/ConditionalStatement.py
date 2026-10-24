# .  Use conditional statements to solve: (a) write a program that tests whether a given number is
# positive, negative or zero; (b) write an if-else program that determines whether a number is even
# or odd.




number = int(input("Enter number : "))
if number <0:
  print("number is negative :" , number)
elif number>0:
  print("number is positve :", number)
else:
  print("number is zero")    
  
  
# find the even odd

if number%2== 0:
  print("the number is even :" , number)
else:
  print("the number is odd :", number)    