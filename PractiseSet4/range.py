# 9.  Make use of logical conditions: (a) write a program that tests whether a number falls inside a
# specified range; (b) write a program that tests whether a number can be divided by both 2 and 3

number = int(input("Enter your number : "))

if number>=0 and number<=100:
  print("the number is between 0 and 1 ")
else:
  print("number is outliers")  
  
# divisble 

if number%2==0 and number%3==0:
  print("number is divisble by 2 and 3")
else:
  print("number is not divisible")  

 
  