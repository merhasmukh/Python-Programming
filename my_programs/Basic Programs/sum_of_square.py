num=int(input("Enter A Number To Get Square Up To: "))

total=0
for i in range(1,num+1):
	x=(lambda i:i*i)
	total=total+x(i)
	
print(total)	