
# Automate the Boring Stuff Chapter 0-1
print('Hello World!')

# Generate TypeError: can only concatenate str (not "int") to str
'42' + 3

2+2
2-2
12*12
144/12
2

# 2 to the exponent 2
2**2

# Modulus / remainder (i.e. 22/8's remainder)
22 % 8

# Integer division / floored quotient
22 // 8

# Regular division
22 / 8 

# Math operations follow math precendence, so ** is first, then *, /, //, and % from left to right, then + and - operators
2+3*6
# = 20

(2+3)*6
# = 30

# Invalid syntax
5+
42 + % 4

# a common error, forgot a single quote around a string: SyntaxError: EOL while scanning string literal
'Hello world!

# Combine strings
'Jack'+' and '+'Jill'

# Repeat (replicate) strings, only works with integers, otherwise you will get an error multiplying other strings or floating points (e.g. 5.0)
'Alice'*5

# Storing variables, they must:
# 1. be one word with no spaces
# 2. only use letters, numbers, underscore 
# 3. cannot begin with a number
# Conventions: they are case sensitive and should begin with a lower case letter per convention and use camelcase (e.g. lookLikeThis)
number = 42
number

secondNumber = 5

secondNumber + number

# overwriting existing value, variable overwriting works with strings too
number = number + 5
number

# Conversion of types
print('I am ' + str(29) + ' years old')

str(-3.14)

int('40')

float('3.14')

inputStr = input()
inputStr = int(inputStr)
inputStr*10

# Round down a floating point
int(4.6)
# = 4

# Integers can be compared to floating points, but numbers cannot be compared against strings in terms of value

40 == '40'
# False

40 == 40.0
# True