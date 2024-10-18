
class Account:
 def __init__ (self ,balance):
           self.setbalance(balance)
	
				  
 def setbalance (self ,balance ):
    if balance>0:
		        self.balance=balance		    
	
    else:
          raise ValueError("Invalid balance value: %d" % (balance))
 
 def getbalance (self):
    
		     return   self.balance	  
 def credit (self,amount):
    
		     self.balance=self.getbalance()+amount 		
 def  withdrawal (self,amount):
            if amount<self.getbalance():
		                         self.balance=self.getbalance()-amount
		  
		    
				                      
				       




print("-----------------------------------------")

a=Account(23)
print("----------------------------------------")
print("ACCOUNT BALANCE BEFORE MONEY DEPOSIT")

print ("Our initial  balance is %.2f"%( a.getbalance()))
print("-----------------------------------------")
print("ACCOUNT BALANCE AFTER  MONEY DEPOSIT")
d=float(input("Enter deposit\n"))

a.credit(d)
print ("Our   balance after our deposit  is %.2f"%a.getbalance())
print("-----------------------------------------")

print("ACCOUNT BALANCE AFTER  MONEY WITHDRAWAL")

w=float(input("Enter withdrawal amount \n"))
a.withdrawal (w)
print ("Our   balance after our withdrawal  is %.2f"%a.getbalance())





