# iteraor is an object that is used to allow one element at a time 
myList = [20,30,40,50]
myIterator = iter(myList)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

# generator is a simple way to create an iterator using a function with yeild keyword

def myGenerator():
  yield 10
  yield 20
  yield 30
  yield 40
  
gen = myGenerator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
  