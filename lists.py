#List: list is collection which is ordered and changeable.Allow duplicate  		members.
#Tuple: Tuple is a collection which is ordered and unchangeable.allows 		duplicate members.
#Set:  Set is a collection which is unordered and unindexed. No duplicate 		members.
#Dictionary : is a collection which is unordered,changeable and indexed. 	no duplicate members.

#In Python lists are written with squre brackets.

thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist)

#You can access the list items by referring to the index number

print(thislist[1])
print(thislist[-1])

#you can specify a range of indexes by specifying where to start and where to end the range

print(thislist[2:5])
#remember that the first item has index 0.

print(thislist[:4])
print(thislist[2:])

#range of negative indexes

print(thislist[-4:-1])

#To change the value of a specific item ,refer to the index number

thislist[2]="potato"  #it changes cherry to potatos.....
print(thislist)

#You can loop through the list itemes by using a for loop:

for a in thislist:
 print(a)

#Check if item exists
#To determine if a specified item is present in a list 

if "potato" in thislist:
	print("yes,potato is in the fruits list!")

#To determine how many items in  a list has

print(len(thislist))

#To add an item to the end of the list
thislist.append("orange")
print(thislist)

#To add an item at the specified index
thislist.insert(4,"cherry")
print(thislist)

#There are several methods to remove items from the list

thislist.remove("potato")
print(thislist)

#The pop() method removes the specified index 
#the last item if index is not specified
thislist.pop() 
print(thislist)

#The del keyword removees the specified index

del thislist[0]
print(thislist)

#The del keyword can also delete the list completely

#del thislist    #this will cause an error because you have succsesfully 
#print(thislist)	#deleted "thislist"

thislist.clear()
print(thislist)

mylist=thislist.copy()
print(mylist)


#Join two list

list1= ["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)

#Another way to join lists are by appending all the items from list2 into list1,one by one:

list1=["a","b","c"]
list2=[1,2,3]

for x in list2:
	list1.append(x)
print(list1)
	
	
#You can use the extend() method....

list1=["a","b","c"]
list2=[1,2,3]

list1.extend(list2)
print(list1)

#Using the list() constructor to make a list:
 
list5=list(("apple","banana","cherry")) #note the double round-brackets
print(list5)

