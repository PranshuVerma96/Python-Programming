# this is the simple interest
# principle = Original amount of money 
# Write a program to calculate Simple Interest


principal = int(input("Enter your Orignal amount :"))

# rate Interest rate per year
rate = int(input("Enter Rate : "))

#time = time in years
time = int(input("Enter time : "))

Simple_Interest = (principal * rate * time)/100

print("Simple interest is : " ,Simple_Interest )