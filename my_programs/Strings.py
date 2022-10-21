#pick any random number 
import random
print(random.randrange(1,10))


a="""My name is hasmukh
	My father name is ghanshyambhai
	My mother name is kailashben"""
#multiline string using """.
print(a)


b= "Hello World!"
print(b[6])#sixth number of b


c="Helloworld"
print(b[2:4])#get the character from 2 to position 4(4 not included)

d="hello World"
print(d[-4:-1])

#String length

e="Mer Hasmukh"
print(len(e))

#The strip() method removes any whitespaces from the beginning or the end
f="  hello world  "
print(f.strip())

#the lower() method returns the string in lower case

g="HELLO WORLD!"
print(g.lower())

#The upper() method returns the string in upper case
h="hello world"
print(h.upper())

#The replace() method replaces a strings with another string
i="Hello World"
print(i.replace("H","M"))

#The split() method splits the strings into substrings if it finds instances of the separator
j="Hello World"
print(j.split(","))

#To check if a certain phrase or character is present in a string,we can use the keywords in or not in..
txt = "The rain in Spain stays mainly in the plain"
k= "ain"  in txt
print(k)

#Merge variable l with variable m into variable n.
l="Mer"
m="Hasmukh"
n=l+m
print(n)

#To add a space between them
o="Mer"
p="Hasmukh"
q=o+" "+p
print(q)

#As we learned in the python variables ,we cannot combine stringgs and numberslike this.......


#age =36
#txt ="My name is john, I am "+age
#print(txt)
#error
#but we combine strings and numbers by using format() method!

age=22
txt="My name is hasmukh, and I am {}"
print(txt.format(age))


#The format() method takes unlimited number of arguments and are placed into the respective placeholders:

quantity =3
item_no =567 #blank space is not valid so use '_'.
price = 49.95
myorder="I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,item_no,price))


#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno=567
price = 49.95
myorder="I want to pay {2} dollars for {0}  pieces of item {1}."
print(myorder.format(quantity,itemno,price))

#You  will get an error if you use double quotes inside a string that is surrounded by double qutoes:
#txt="We are the so-called "vikings" from the north."
#print(txt)
#error

#to fix this program,use the escape character \".


#the escape charcter allows you to use double quotes when you normally would not be allowed:

txt="We are the so-called \"Vikings\" from the north."
print(txt)

#other escape characters used in python:

# \' Single Quote
# \\ Backslash
# \n new line
txt="my name is \'hasmukh\' and i like to\\ study about computer \n and technology."
print(txt)

# \r removes word from back and put it on start up of statements
# \t tab
# \b Backslash
# \f Form Feed
txt="i \f am from small village \r of gujrat state\t in india."
print(txt)




