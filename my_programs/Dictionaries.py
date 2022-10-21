# A Dictionary is a collection which is unordered, changeable and indexed. in python dictionaries are written with curly brackets and they have keys and values.


dict1={
"brand" : "ford",
"model" : "mustang",
"year"  : 1964
}

print(dict1)

# Accessing Items

a=dict1["year"]
print(a)


# There is also a mrthod called get() that will give you the same result

b=dict1.get("model")
print(b)

# Change Values

dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict2["year"] = 2018
print(dict2)

# Loop Through a Dictionary
# When looping through a dictionary ,the retunrn value are the keys of the dictionary

for x in dict2:
 print(x)

# print all values in the dictionary,one by one.....

for x in dict2:
 print(dict2[x])

# You Can also use the values() function to return values of a dictionary

for x in dict2.values():
 print(x)

# loop through both keys and values by using the items() function

for x,y in dict2.items():
 print(x,y)

# To determine if a specified key is present in a dictionary use in keyword

dict2={
"brand" : "ford",
"model" : "mustang",
"year"  : 2018
}

if "model" in dict1:
      print("Yes")

# Dictionary length

print(len(dict2))

# Adding Items

dict2={
"brand" : "ford",
"model" : "mustang",
"year"  : 2018
}

dict2["color"]="red"
print(dict2)

# Removing Items

dict2={
"coler"  :"red",
"brand" : "ford",
"model" : "mustang",
"year"  : 2018
}
dict2.pop("model")
print(dict2)

# del keyword removes the items with the specified key name

dict2={
"coler"  :"red",
"brand" : "ford",
"model" : "mustang",
"year"  : 2018
}

del dict2["year"]
print(dict2)


# Copy a Dictionary
 
dict2={
"coler"  :"red",
"brand" : "ford",
"model" : "mustang",
"year"  : 2018
}

dict3=dict2.copy()
print(dict3)

# Another Way

dict2={
"coler"  :"red",
"brand" : "ford",
"model" : "mustang",
"year"  : 2018
}

dict4=dict(dict2)
print(dict4)


# Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "hasmukh",
    "year" : 1997
  },
  "child2" : {
    "name" : "amit",
    "year" : 1998
  },
  "child3" : {
    "name" : "kapil",
    "year" : 2000
  }
}

print(myfamily)

# The dict() Constructor

dict5=dict(name="hasmukh",surename="mer",year="22")
print(dict5)

