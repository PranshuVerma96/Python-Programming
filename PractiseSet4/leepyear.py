# 12.  Use conditional statements to solve: (a) write a program that checks if a year meets the standard
# leap-year rules; (b) write a program that places a person's age in the child, teenager or adult
# category.

year = int(input("Enter the year : "))
if year %400 == 0:
  print(" year is leap year")
elif year %100 ==0:
  print(" year is  not leap year")
elif (year %4==0) :
  print(" year is leap year")
     
else:
  print("year is not leap year")  
 
# progra for check teengar and adualt 

age = int(input("Enter your age : "))
if age <13:
  print("child")
elif age <18:
  print("Teenager")   
else:
  print("adult") 