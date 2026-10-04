# write a program to check whether student has passed using a depend passed marked
marks = int(input("Enter the marks :"))

if(marks<0 or marks >100):
  print("Invalid marks")
  
if(marks >= 90):
  print("Grade A and Execellence")
elif(marks<=89 and marks):