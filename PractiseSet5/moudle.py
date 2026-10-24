# Analyse how modules are used: (a) contrast the import math approach with the from math import
# ... approach; (b) discuss how two suitable functions of the Math module can make numerical
# calculations easier.

# module is code bulde that is used to perfom some specific task it reduce the size of code it icrease the code readiablity 

import calculation 

calculation.sum(10,20)
calculation.division(10,2)
calculation.subTraction(10,4)
calculation.multiply(10,4)


# building module this is also code of bundle 
# which is alread writen by developer in pyton and we can use it in my code easily

import math
print(math.sqrt(81))
print(math.ceil(9.33))
print(math.floor(233.22))
print(math.factorial(4))

# we can also imprort  
import math as m 
print(m.cbrt(343))

from math import sqrt

print(sqrt(40))