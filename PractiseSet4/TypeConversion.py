# 2.  Show how data types and type conversion are used: (a) take an integer and a floating-point value
# as input and print the type of each; (b) convert appropriate input values, then compute their total
# and average.

# data types tell types of data want to perform operation 
# data types conversion is a process to convert a type of data into another type 




number = int(input("Enter number : "))
print(type(number))
print(number)

number1 = float((input("Enter number : ")))
print(type(number1))
print(number1)

number2 = int(input("Enter the number: "))
number3 = int(input("Enter second number : "))
number4 = int(input("Enter third number : "))

total = number2 + number3 + number4
print("total is : " , total)
average = float(total/3)
print("the average is : ", average)
