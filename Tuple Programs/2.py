
t1=(-1,0,1,2,3,4,5,6,7,8,9,10,12,23,34,45,50,60,90,100,30)
no=int(input("Enter How Many Max Elements You Want.. :"))
t1=sorted(t1)
i=len(t1)-1
while(no!=0):
	print(t1[i])
	i-=1
	no-=1

	
t1=(-1,0,1,2,3,4,5,6,7,8,9,10,12,23,34,45,50,60,90,100,30)
no=int(input("Enter How Many Min Elements You Want.. :"))
t1=sorted(t1)
i=0
while(no!=0):
	print(t1[i])
	i+=1
	no-=1	
	
