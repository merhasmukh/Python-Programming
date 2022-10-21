
def primeNumbers(no):
	
	if no >1:	
		for i in range(2,int(no/2)+1):
			if no%i == 0:
				return "Not a Prime Number"
		return "prime Number"					
	else:
		return "Not A prime NUmber"	

num = int(input("Enter A Number: "))
if num > 0:
	print(primeNumbers(num))	
else:
	print("Not A Valid Number..!!!")			