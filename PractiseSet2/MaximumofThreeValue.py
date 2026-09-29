#define function with parameters and return values 
# maximum of the three number


def maxiMumOfThree(num1 ,num2, num3):
  if(num1 >= num2 and num1 >=num3):
    return num1
  elif (num2 >= num1 and num2 >=num3):
    return num2
  elif(num3 >= num1 and num3 >= num2):
    return num3


  # call a function 
  
result = maxiMumOfThree(2,5,3)
print("the greater number is :" , result)
   