# 6.  Use elif and nested if statements: (a) write a program that gives a basic grade based on marks; (b)
# write a program that finds the greatest of three numbers with nested conditions

marks = int(input("enter marks : "))
if marks >= 40:
  if marks>=90:
    print("Grade A")
  else:
    if marks>=80:
      print("Grade B")
    else:
      if marks>=70:
        print("Grade C")
      else:
        print("Grade D")
else:
  print("Fail")                   
  
  # Find the greatest of three numbers using nested if

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2:
    if number1 > number3:
        print("Greatest number is:", number1)
    else:
        print("Greatest number is:", number3)
else:
    if number2 > number3:
        print("Greatest number is:", number2)
    else:
        print("Greatest number is:", number3)