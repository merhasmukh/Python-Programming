
def primeNumbers(no):
	
	if no >1:	
		for i in range(2,int(no/2)+2):
			if no%i == 0:
				break
			print(no)
			break					
	else:
		pass
			

print("Enter The Range to Print All The Prime Number :")
num1 = int(input("Enter  First Number : "))
num2 = int(input("Enter Second Number: "))

for number in range(num1,num2):	
	if number > 0:
		primeNumbers(number)	
	else:
		print("Not A Valid Number..!!!")			