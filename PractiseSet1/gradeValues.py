#Assign grades based on marks using `if-elif-else`.

number = int(input("Enter yours marks : "))

if(number <0 or number >100):
  print("Invalid marks")
elif(number >= 90):
  print("Grade A")
elif(number >=70):
  print("Grade B")
elif(number >=60):
  print("Grade C")
elif(number >=50):
  print("Grade D")
else:
  print("Fail")      