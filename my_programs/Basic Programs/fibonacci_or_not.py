a,b=0,1
list1 = []
for i in range(0,100):
	list1.append(a)
	no=a+b
	a=b
	b=no
	

number=int(input("Enter The Value To Check It is Fibonacci Or Not..: "))
	
for x in list1:
	if x==number:
		print("It's A Fibonacci Number")
		break
	else:
		pass
			