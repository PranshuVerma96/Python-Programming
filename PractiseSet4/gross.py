# 11.  Show calculations based on input: (a) write a program that finds the gross amount from a given
# quantity and price; (b) apply a basic discount condition and print the final amount to be paid.

item = int(input("Enter the number of item : "))
price = int(input("Enter the price per item : "))
gross_amount = item * price
print("gros amount " ,   gross_amount)

# calculate the discount 
if gross_amount >= 1000:
  discount = gross_amount*10 /100
  print("the discount is " , discount)
else:
    discount = 0
    