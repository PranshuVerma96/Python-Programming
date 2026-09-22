# Write a program to calculate Compound Interest.

# principle original amout
principle = float(input("Enter your anount  : "))

# rate rate of interest (per year)
rate = float(input("Enter your rate : "))

# time time in years
time = float(input("Enter your time "))

final_Amount = principle*(1 + rate/100)**time

print("Final amount : ", final_Amount)

Compound_Interest = final_Amount - principle

print("Compound Interest is " , Compound_Interest)