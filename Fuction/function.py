# # 12.  Analyse how functions behave: (a) discuss the way arguments hand values over to a
# # # user-defined function; (b) contrast a function that prints its result with one that returns its result

# # function is a block of code that is used for specific task .
# # that is used to impore the code quality 
# # it is define using the def keyword 
# # do not need to write a code multiple times

# # this is a function with no parater

# def greet():
#   print("Hello Python ")
  
# greet()  

# # Positional Arguments 
# def describe_pet(animal_type, pet_name):
#   print(f"I have a animal {animal_type} named {pet_name}")

# describe_pet("dog","Tony")  

# # keyword arguments with keyword arguemtns you expicitly assign the value to the parameter name when calling the function. because of this. the order no longer matters.

# def createSum(number1 , number2):
#   print(f"I have to number it's sum is {number1 + number2}")
  
# createSum(number1=45, number2= 50)  
  
# # default arguments
# def printName(name = "Dia"):
#   print(name)

# printName("Pranshu")
# printName() 


def greater(a,b):
  if(a>b):
    print(a, "is greater")
  else:
    print(b ," is greater")
      
    
greater(5,9)    
def calGmea(a,b):
  mean = (a*b)/(a+b)    
  print(mean)
 
calGmea(9,4) 

def average(a,b):
  print("the average is ", (a+b)/2)
  
average(4,3)  

# default argument 
def sum(a=9,b=8):
  print(a+b)

sum(93,23)
sum()
sum(5)

# keyword arguments 
def average(a = 9, b= 3):
  print((a+b)/2)

average()
average(b=3,a=2)

# required argument
def sum(a,b=1,c=4):
  print((a+b+c))

sum(1) 

# variable length argument

def average(*number):
  print(type(number))
  sum = 0
  for i in number:
    sum = sum + i 
  print("average is " , sum /len(number))
  
average(2,3,4,5,34,2)  

def name(**name):
  print("Hello " , name["fname"],
        name["mname"],name["lname"]
        )
  

name(mname = "pranshu",lname= "Alok" ,fname = "barnes")  

