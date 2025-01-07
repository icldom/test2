
class Bank:
	def __init__(self,name,balance):
		#class bank has attribute name and balance (starting balance is zero)
		self.name = name
		self.balance = 0

	def deposit(self,amount):
		#insert amount to balance
		self.balance += amount

	def withdraw(self,amount):
		if self.balance > amount:
			self.balance -= amount
		else:
			print(f"xxxx")
		#withdraw amount from balance
		print(f"Balance after withdraw in the {self.name} account is {self.balance}.")

#create instance class bank
bank = Bank("TatraBanka",0)
#insert 2000
bank.deposit(2000)
#withdraw 500
bank.withdraw(500)