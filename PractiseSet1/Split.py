# Split the string into words and join the words using a separator.

from unittest import result


myName = "my name is pranshu"

#spliting the given string
data = myName.split()
print(data)


# join method

firstStr = ["my" , "name", "is","pranshu"]
result = "".join(firstStr)
print(result)

data = "shivam ,Rahul, ram"
item = data.split(",")
print(item)
