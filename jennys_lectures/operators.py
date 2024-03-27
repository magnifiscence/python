# types of operators in python include arithmetic, comparison(relational),
# logical, bitwise, assignment, identity, membership
# thesame like BODMAS we use PEMDAS(parenthesis, exponent, division, multiplication,add, subtraction)

# Arithmetic operators +, -, /, %, *, **, ()
print(5/2)
print(5**2)
print(5%2)

# Assignment and comparison operators
a,b=4,3
d=5
c=a+b
a+= 2
c /= a # this prints a whole number rather than a float c //= a
print(c)
print(d==5)
print(d<=5)
print(d<5)
print(d != 5)

# logical operators: and, or, not
a,b=5,4
print()
print(a>4 and b<5)
print(a>4 or b<10)
p = False
print(not(p))
print(not(False))

# bitwise operators &and or| ^XOR ~NOT <<leftshift >>rightshift
# in leftshift we gain bits with the formular X*2**n leftshift x/2**n
# in bitwise operators ~m = -(m + 1)
x,y=5, 4
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 2)
print(x >> 2)
print(~45)
print(id(x))
print(x is not y)
# identy operators in python include = and ==
z = 3
w = 3
z=w
z==w

# membership operator they include "in" and "not in"
str = 'jerry'
list=[1,2,3,4,5]
print("y" in str)
print('je' in str)
print('J' not in str)
print( 20 in list)
print (1 in list)
print ( 1 not in list)

