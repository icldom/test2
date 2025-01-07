class Factory:
	def __init__(self,name):
		self.name = name
		self.employes_no = 0
		self.knowhow = []

	def set_eployes_no(self, new_no):
		self.employes_no = new_no

	def add_HR(self):
		self.employes_no += 4

	def add_shift(self):
		self.employes_no += 30

	def exchange_knowhow(self, another_factory):
		self.knowhow.extend(another_factory.knowhow)
		pass

rolex = Factory("Rolex")
rolex.set_eployes_no(40)
rolex.add_HR()
rolex.add_shift()
rolex.add_shift()
rolex.knowhow.append("purity")
print(f"Factory {rolex.name} has {rolex.employes_no} employees.")
ikea = Factory("Ikea")
ikea.add_shift()
ikea.knowhow.append("accuracy")
rolex.exchange_knowhow(ikea)
print(f"Factory {rolex.name} has knowhow {rolex.knowhow}.")