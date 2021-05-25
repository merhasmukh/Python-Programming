

def simpleInterest(Money,Years,Irate):
	I=(Money * Years * Irate)/100
	return I
	
value=int(input("Enter Value: "))
year=float(input("Enter Years : "))
rate=float(input("Enter Rate: "))

print(simpleInterest(value,year,rate))	