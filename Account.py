
class Account:
 def __init__ (self ,balance):
           self.setbalance(balance)
	
				  
 def setbalance (self ,balance ):
    if balance>0:
		        self.balance=balance		    
	
    else:
          raise ValueError("Invalid hour value: %d" % (balance))
 
 def getbalance (self):
    
		     return   self.balance	  
 def credit (self,amount):
    
		     self.balance=self.getbalance()+amount 		


print("-----------------------------------------")

a=Account(23)
print("ACCOUNT BALANCE BEFORE MONEY DEPOSIT")

print ("Our initial  balance is %.2f"%( a.getbalance()))

print("ACCOUNT BALANCE AFTER  MONEY DEPOSIT")
d=float(input("Enter deposit\n"))

a.credit(d)
print ("Our   balance after our deposit  is %.2f"%a.getbalance())
