
class Worker:
	def __init__(self,name,surname,plat):
		self.name = name
		self.surname = surname
		self.plat = plat

	def payout(self,how_much):
		self.plat += how_much

	def printit(self):
		print(f"Worker {self.name} {self.surname} got paid {self.plat} in euros.")

animal = Worker("Dominik","AnimalPK",6000)
animal.payout(5000)
animal.printit()

shaker = Worker("Stratimir","dPartyShaker",5000)
shaker.payout(11000)
shaker.printit()









