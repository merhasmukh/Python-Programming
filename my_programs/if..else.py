# In this chapter we study about if...else conditions.....

a=200
b=200
if b>a:
 print("b is greater than a")
elif a==b:
 print("a and b are equal")
else:
 print("b is less than a")

# One line if else statements...............
c=256
d=220
print("A") if c>d else print("B")


# One line if else statements with 3 conditions.........

e=330
f=330
print("A") if e>f else print("=") if a==b else print("B")


# AND

g=200
h=33
i=500
if g>h and i>h:
 print("Both conditions are true")

#OR

j=455
k=200
l=100
if j>k or j<l:
 print("At least one of the conditions is true")

# Nested If

m=11

if m>10:
 print("Above ten")
 if m>20:
  print("and also above 20!")
 else:
  print("but not above 20.")