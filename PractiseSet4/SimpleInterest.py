# calculate the simple interest
principle = float(input("Enter your amount : "))
rate = float(input("Enter your rate :"))
time = float(input("Enter your time in years : "))

simpleInterest = (principle * rate * time)/100
print("Simple Interest is : ", simpleInterest)