# 7.  Use arithmetic operators to solve: (a) write a program that finds the area of a circle for a radius
# entered by the user; (b) write a program that computes the square and the cube of a number.

radius = float(input("Enter radius : "))

areaOfSqure = 3.14*(radius*radius)
print(areaOfSqure)

number = float(input("Enter your number : "))
cube = number * number * number
print("cube is : " ,  cube)
square = number * number
print("square is : ", square)

cube = lambda x : x*x*x
print(cube(5))

square = lambda y : y*y
print(square(5))