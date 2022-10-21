count=0
a,b=0,1
list1 = []
for i in range(0,10):
	list1.append(a)
	no=a+b
	a=b
	b=no

mul=int(input("Enter The Multiple No..: "))
nth=int(input("Enter the Nth Multiple..: "))

for i in list1:
	if count!=nth:
		if i%mul==0:
			count+=1
		else:
			pass
	else:
		pass
print(i)						




	
	
