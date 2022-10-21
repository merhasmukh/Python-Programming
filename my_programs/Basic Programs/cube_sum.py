num=int(input("Enter A Number To Get Cube Sum: "))

total=0
for i in range(1,num+1):
	x=(lambda i:i*i*i)
	total=total+x(i)
	
print(total)	