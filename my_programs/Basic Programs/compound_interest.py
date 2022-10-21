

def compoundInterest(Money,Years,Irate):
		Amount = Money*(1+(Irate/100))**Years
		return Amount-Money
		
		
amt=int(input("Enter Amount: "))
year=int(input("Enter Years : "))
rate=int(input("Enter Rate: "))


print(compoundInterest(amt,year,rate))