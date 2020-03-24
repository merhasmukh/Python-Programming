#Boolean represent one of two values : True or false.
#You can evaluate any expression in python, and get one of two answers, True or False.


print(10>9)
print(10==9)
print(10<9)

#print a message based on whether the condition is True or false:

a=200
b=33
if b>a:
	print("b is greater than a")
else:
	print("b is not greater than a")

#The bool() function allowa you to evaluate any value, and give you true or False in return,


print(bool("Hello"))
print(bool(15))

#Evaluate two variables

c="Hello"
d=15
print(bool(c))
print(bool(d))

#Any string is True,except empty strings.
#Any number is true, except 0.
#Any list,tuple,set and dictionary are True,except empty ones.

bool("abc")
bool(0)
bool(["apple","cherry","banana"])
print(bool("abc"))
print(bool(0))
print(bool(["apple","cherry","banana"]))

#The following will return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))

#Python also has many built-in functions that returs a boolean value,like the isinstance() function whiich can be used to determine if an object is of a certain data type

e=200
print(isinstance(e,int))

