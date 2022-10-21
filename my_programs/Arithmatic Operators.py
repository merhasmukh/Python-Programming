#Operators are used to perform operations on variables and values.

#Arithmatic Operators
#Arithmatic operators are used with numeric values to perform commom mathematical operations:


a=5.2
b=2
print(a+b)	#addition
print(a-b)	#Substraction
print(a*b)	#Multiplication
print(a/b)	#Division
print(a%b)	#Modulus
print(a**b)	#Exponentiation
print(a//b)	#Floor division


#Assignment Operators
#assignment operators are used to assign values to variables:

c=5 	  
c+=3 #=c+3

d=5
d-=3 #d=d-3

e=5
e*=3 #e=e*3

f=5
f/=3 #f=f/3

g=5
g%=3 #g=g%3

h=5
h//=3 #h=h//3

i=5
i**=3 #i=i**3

j=5
j&=3  #j=j&3

k=5
k|=3 #k=k|3

l=5
l^=3 #l=l^3

m=5
m>>=3 #m=m>>3

n=5
n<<=3 #n=n<<3
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)


#Comparison Operators
#return boolean value

o=6
p=8
print(o==p)
print(o!=p)
print(o>p)
print(o<p)
print(o>=p)
print(o<=p)

#Logical Operators
#Logical operators are used to combine conditional statements:

q=10
r=15
print(q<r and q>r)
print(q<r or q>r)
print(not(q<r and q>r))

#Identity Operators
#Identity operators are used to compare the objects,not if they are equal ,but if they are actually the same object ,with the same memory location:

s=["apple","banana"]
t=["apple","banana"]
u=s
print(s is t) #return False because s is not the same object as t,even if 			they have same content
print(s is u)#returns True because u is the same object as s
print(s == t)#to demonstrate the difference between "is" and "==": thid 		comparison returns True because s is equal to u.

#Membership Operators
v=["apple","banana"]
print("apple" in v)	
print("mango" not in v)

#Bitwise Operators

# & AND Sets each bit to 1 if both bits are 1
# | OR  Sets each bit to 1 if one of two bits is 1
# ^ XOR Sets each bit to 1 if only one of two bits is 1
# ~ NOT Inverts all the bits
# <<  Shift left by pushing zeros in from the right and let the leftmost 	bits fall off
# >>   Shift right by pushing copies of the leftmost bit in from the left 	and let the rightmost bits fall off

