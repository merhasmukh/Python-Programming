number=input("Enter A Number: ")
list1=[]
total=0
count=0
no=0
for i in number:
	list1.append(i)
	count+=1

for i in list1:
	no=(int(i)**count)
	total=total+no

	
if int(number)==total:
	print("Armstrong")
else:
	print("Not Armstrong")		
	
