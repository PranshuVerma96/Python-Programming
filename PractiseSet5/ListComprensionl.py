numbers = [1, 2, 3, 4, 5]

squares = [i * i for i in numbers]

print(squares)


from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# 1. map() - Find the square of each number
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# 2. filter() - Find even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# 3. reduce() - Find the sum of all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

# 4. find() - Find the position of a character in a string
text = "python programming"
position = text.find("p")
print("Position of p:", position)

