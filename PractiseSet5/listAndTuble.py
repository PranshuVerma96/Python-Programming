# 1.  Analyse Python collections: (a) discuss the situations where a list suits changing data better than
# a tuple; (b) contrast a set with a list for holding unique values and justify which is the better
# option

# list is ordered colleticon of data item where data is sorted ordered wise and that conatin all types of data types
# list is multable and we can easly update and modify the list 

# tuple is also ordered colletcion of data item it store all type of data but it is not mutalble you cannot change and modify.

# we have a case there are a record of student and we want to sorte the data in the collection here list is best for me beaceuse if any student has been faild and there no marks in list onfly faild is commes than which student take the reexam and after that we need to update the collection to change the marks here is list is the suidtable to store data 

# and we have another case where the we want to store the imublage data like we store.

list = [20,30,40,50,"Failed"]
print(list)
list[4]= 90

print(list)

# tuble 
mytuple = (1,2,3,4,5)
print(mytuple)

# comparison between list and set 
# list is oredered cllection of data,here we can sorte all types of data 

# list is mutable 
# list element can accessed by index
# list insert the element ordered wise which one you gave 

# set 
# set is nonordered collection of data it sorte the data no oreder
# you can insert the element it insert the element rendom 

set = {1,3,4,5}
set.add(40)
print(set)