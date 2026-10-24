# .  Use Python variables and operators to answer: (a) write a program that takes two numbers as
# input and shows their sum, difference, product and quotient; (b) write a program that computes
# simple interest from values entered by the user.

# variable is a container that is used for store data and perform operation on them.
# opertors are specific symbol that has its predefine meaning and that are used to perform specfic task.

number1 = float(input("Enter first number : "))
number2 = float(input("Enter Second number : "))

sum = number1 + number2
print("Sum is: ",sum)

multiply = number1* number2
print("multiply is : ", multiply)

if number2!=0:
  division = number1/number2
  print("Division is : ", division)
else:
  print("Invalid Case")

subTraction = number1 - number2
print("subtraction is : " , subTraction)    

quotient = number1 // number2
print("quotient is : ", quotient)