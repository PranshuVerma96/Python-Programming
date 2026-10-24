# 5.  Show the use of user input and expressions: (a) write a program to find the area and perimeter of
# # a rectangle; (b) write a program that converts a temperature from Celsius into Fahrenheit


# program for perimenter of rectangle
from operator import le
from tkinter import W


length = float(input("Enter length : "))
width = float(input("Enter Width : "))

perimeter = 2 * (length + width)
area = length * width
print("area is : ", area)
print("the permeter is : ", perimeter)


temperature = float(input("Enter the temperature in fahrenheit : "))
# convert celcius to fahrenheit 
celcius = (temperature - 32)*5/9
print("temberature in celcius : " , celcius)

temperature1 = float(input("Enter the temperature in celcius : "))
fahrenheit = (temperature1 * 9/5)+32
print("temperature is fahrenheit : ", fahrenheit)
