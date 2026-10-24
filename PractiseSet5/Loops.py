# 4.  Analyse the choice of loops: (a) contrast a for loop with a while loop when the number of
# repetitions is fixed; (b) discuss a simple scenario in which a nested loop is needed


# loop is used to iterate of all collection of data
# for loop 
# while loop 

# for loop when we use this we know time we iterate the loop 

list = [10,20,30,40]
for item in list:
  print(item)
# while loop used when we do not kown the certion iteration condtion 


item = 0
while item <len(list):
  print(list[item])
  item += 1
  
for i in range(1,4):
  for j in range(1,4):
    print("*" ,end=" ")  
  print()  
  