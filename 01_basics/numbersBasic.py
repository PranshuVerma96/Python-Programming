# >>> result = 1/3.0
# >>> result
# 0.3333333333333333
# >>> repr('chai')
# "'chai'"
# >>> str('chai')
# 'chai'
# >>> print('chai')
# chai
# >>> x = 4
# >>> y= 2
# >>> x>y
# True
# >>> x<y
# False
# >>> 5.0 == 5.0
# True
# >>> 5.0 == 5
# True
# >>> 4.0 != 5.0
# True
# >>> 5.0 != 5.0
# False
# >>> x, y, z
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     x, y, z
#           ^
# NameError: name 'z' is not defined
# >>> z= 4
# >>> x, y, z
# (4, 2, 4)
# >>> x<y<z
# False
# >>> x <y and y<z
# False
# >>> x >>1
# 2
# >>> x>>3
# 0
# >>> x>>5
# 0
# >>> 1 == 2 <3
# False
# >>> import math
# >>> math.floor(4.0003)
# 4
# >>> math.ceil(4.2232)
# 5
# >>> math.floor(-3.5)
# -4
# >>> math.floor(-3.2)
# -4
# >>> math.ceil(-4.3)
# -4
# >>> math.trunck(2.8)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     math.trunck(2.8)
#     ^^^^^^^^^^^
# AttributeError: module 'math' has no attribute 'trunck'. Did you mean: 'trunc'?
# >>> math.trunc(2.4) 
# 2
# >>> math.trunc(-2.8)
# -2
# >>> 99999999 + 1
# 100000000
# >>> 9*43
# 387
# >>> 2**200      
# 1606938044258990275541962092341162602522202993782792835301376
# >>>  2+ 2j
#   File "<stdin>", line 1
#     2+ 2j
# IndentationError: unexpected indent
# >>> 2 + 2j
# (2+2j)
# >>> 2 + 2j *3
# (2+6j)
# >>> (2+2j)*4
# (8+8j)
# >>> 0O20
# 16
# >>> 0b1000
# 8
# >>> 01bb0
#   File "<stdin>", line 1
#     01bb0
#     ^
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# >>> 9^8
# 1
# >>> 8
# 8
# >>> repr('chai'       
# ... hex(58)
#   File "<stdin>", line 1
#     repr('chai'
#          ^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> hex(64)
# '0x40'
# >>> bin(34
# ... int('1000' ,2)
#   File "<stdin>", line 1
#     bin(34
#         ^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# >>> int('1000' ,2)
# 8
# >>> x = 1
# >>> x << 1
# 2
# >>> x << 9
# 512
# >>> x | 2
# 3
# >>> import random 
# >>> random.random()
# 0.13340082656752006
# >>> random.random()
# 0.32717006649430147
# >>> random.random()*10
# 8.664555020922624
# >>> random.random()*108 
# 59.931157348507725
# >>> random.randint(1,100)
# 66
# >>> random.randint(1,100)
# 94
# >>> random.randint(1,100)
# 9
# >>> random.randint(1,100)
# 5
# >>> random.randint(1,100)
# 81
# >>> random.randint(1,100)
# 19
# >>> random.randint(1,100)
# 56
# >>> random.choice()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     random.choice()
#     ~~~~~~~~~~~~~^^
# TypeError: Random.choice() missing 1 required positional argument: 'seq'
# >>> l = ['leman','chai','masala','mint','ginger']
# >>> random.choice(l)
# 'masala'
# >>> 
# >>> random.choice(l)
# 'chai'
# >>> random.choice(l)
# 'mint'
# >>> random.choice(l)
# 'ginger'
# >>> random.choice(l)
# 'masala'
# >>> random.shuffle(l)     
# >>> l
# ['mint', 'ginger', 'masala', 'leman', 'chai']
# >>> 1
# 1
# >>> 1
# 1
# >>> l
# ['mint', 'ginger', 'masala', 'leman', 'chai']
# >>> l
# ['mint', 'ginger', 'masala', 'leman', 'chai']
# >>> l
# ['mint', 'ginger', 'masala', 'leman', 'chai']
# >>> l
# ['mint', 'ginger', 'masala', 'leman', 'chai']
# >>> 0.1 = 0.1 + 0.4   
#   File "<stdin>", line 1
#     0.1 = 0.1 + 0.4 
#     ^^^
# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# >>> 0.1 +.4 + .4 +.2 - .3 
# 0.8
# >>> .1 + .1 + .1 - .3
# 5.551115123125783e-17
# >>> from decimal import Decimal
# >>> Decimal('0.1') + Decimal('.1') + Decimal('.1)
#   File "<stdin>", line 1
#     Decimal('0.1') + Decimal('.1') + Decimal('.1)
#                                              ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> Decimal('0.1') + Decimal('.1') + Decimal('.1')
# Decimal('0.3')
# >>> Decimal('0.1') + Decimal('.1') + Decimal('.1') - Decimal('.3
#   File "<stdin>", line 1
#     Decimal('0.1') + Decimal('.1') + Decimal('.1') - Decimal('.3
#                                                              ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> Decimal('0.1') + Decimal('.1') + Decimal('.1') - Decimal('.3)
#   File "<stdin>", line 1
#     Decimal('0.1') + Decimal('.1') + Decimal('.1') - Decimal('.3)
#                                                              ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> Decimal('0.1') + Decimal('.1') + Decimal('.1') - Decimal('.3')
# Decimal('0.0')


# >>> setone = {1,2,3,4}
# >>> settwo = {5,6,7,8}
# >>> setone & settwo
# set()
# >>> setone |  settwo
# {1, 2, 3, 4, 5, 6, 7, 8}
# >>> setone -  settwo
# {1, 2, 3, 4}
# >>> setone
# {1, 2, 3, 4}
# >>> setone - {1,2,3,4}
# set()
# >>> type({})
# <class 'dict'>
# >>> type(setone)
# <class 'set'>
# >>>  type(True)
#   File "<stdin>", line 1
#     type(True)
# IndentationError: unexpected indent
# >>>  type(True)
#   File "<stdin>", line 1
#     type(True)
# IndentationError: unexpected indent
# >>> type(True)
# <class 'bool'>
# >>> True is 1
# <stdin>-112:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> True 
# True
# >>> True + 5
# 6
# >>> 