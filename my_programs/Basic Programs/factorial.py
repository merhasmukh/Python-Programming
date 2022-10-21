
def fact(no):
	if no==0:
		return 1
		
	elif no > 0:
		return no * fact(no-1)
	else:
		return "not Possible"	
			
num=int(input("Enter  Number: "))
print(fact(num))
