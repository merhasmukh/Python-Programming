list1=[]
a,b=0,1
for i in range(0,100):
	list1.append(a)
	no=a+b
	a=b
	b=no
        
        
number=int(input("Enter nth number of fibancci: "))

print(list1[number-1])   
