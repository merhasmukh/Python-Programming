#A Set is a Collection which is unorederd and unindexed. In Python Sets are written with curly brackets.

# Sets are unordered so you cannot be sure in which order the items wiil apear

set1= {"apple","banana","cherry"}
print(set1)




set2={"apple","banana","cherry"}

for y in set2:
  print(y)

# Check if "banana" is present in the set

set3={"apple","banana","cherry"}
print("banana" in set3)

# Once a set is created , You cannot change its items but you can add new items

# To add one item to a set use the add() method
# To add more than one item to a set use the update() method


set4={"apple","banana","cherry"}
set4.add("orange")
print(set4)


set5={"apple","banana","cherry"}
set5.update(["orange","mango","grapes"])
print(set5)

# Get the length of a  set

set6={"apple","banana","cherry"}
print(len(set6))

# Remove Item

set7={"apple","banana","cherry"}
set7.remove("banana")
print(set7)


set8={"apple","banana","cherry"}
set8.discard("apple")
print(set8)

# The clear() method empties the set

set9={"apple","banana","cherry"} 
set9.clear()
print(set9)

# The del keyword will delete the set completely

'''set10={"apple","banana","cherry"}
del set10
  print(set10) #this will raise an error because the set no longer exists'''

# Join Two Sets

set11={"apple","banana","cherry"}
set12={1,2,3}
set13=set11.union(set12)
print(set13)

set14={"apple","banana","cherry"}
set15={1,2,3}
set14.update(set15)
print(set14)

# The Set Constructor

set15=set(("apple","banana","cherry"))
print

