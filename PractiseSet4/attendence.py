# 4.  Make use of comparison and logical operators: (a) write a program to decide whether a student
# passes based on a specified pass mark; (b) write a program that checks eligibility on the basis of
# both marks and attendance

from sqlite3 import adapt


marks = int(input("Enter your marks : "))

# if marks>=90:
#   print("Grade A")
# elif marks >= 80:
#   print("Grade B")
# else:
#   print("Failed")    
  
if marks>= 40 and marks <=100:
  print("Student is pass")
else:
  print("Student is fail")    
 
 
  #  check the eligibility 
attendence = int(input("Enter your attendence : "))
if attendence>= 40  and attendence >= 70:
  print("your are eligible ")
else:
  print("Your are not eligible")    