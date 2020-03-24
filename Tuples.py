# A tuple is a collection which is ordered and unchangeable. in python tuples are written with round brackets.

tuple1=("apple","banana","cherry")
print(tuple1)

# You can access tuple items by referring to yhe index number,inside square brackets.

tuple2=("apple","banana","cherry")
print(tuple2[2])

# Negative indexing means beginning from the end. -1 refers to the last item

tuple3=("apple","banana","cherry")
print(tuple3[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.

tuple4=("apple","banana","cherry","orange","kiwi","melon","mango")
print(tuple4[2:5]) # 2(included) and 5(not included)


# Range of Negative Indexes

tuple5=("apple","banana","cherry","orange","kiwi","melon","mango")
print(tuple5[-4:-1]) # -4 (included) and -1 (not included)

# Change Tuple Values
# Once a tuple is created, you cannot changes its value
# You can convert the tuple into a list ,change the list and convert the list back in to tuple

a=("apple","banana","cherry")
b=list(a)
b[1]="kiwi"
a=tuple(b)
print(a)

#loop through a tuple

tuple6=("apple","banana","cherry")
for x in tuple6:
 print(x)

# Check if Item Exists

tuple7=("apple","banana","cherry")
if "apple" in tuple7:
   print("Yes")

# Tuple Length

tuple8=("apple","banana","cherry")
print(len(tuple8))

# Add items
# You cannot add items to a tuple

#tuple9=("apple","banana","cherry")
#tuple9[3]="orange"  #This will raise an error 
#print(tuple9)

# Create Tuple With one Item

tuple10=("apple",)
print(type(tuple10))

tuple11=("apple")
print(type(tuple11))

# Remove Item(You cannot remove items in a tuple..

#tuple12=("apple","banana","cherry")
#del tuple12
#print(tuple12) #this will rais an error because the tuple no longer exists

#join Two tuples

tuple13=("a","b","c")
tuple14=(1,2,3)
tuple15=tuple13+tuple14
print(tuple15)


#The tuple() Constructor

tuple16=tuple(("aaple","banana","cherry")) # Note the double round-brackets
print(tuple16)
