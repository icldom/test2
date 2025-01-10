
#pamatat si min a max cenu
class Predmet:
	def __init__(self,name, min_price, max_price):
		self.name = name
		self.min = min_price
		self.max = max_price
		self.current_price = (min_price + max_price) // 2

	def __str__(self):
		return f"{self.name}: {self.current_price} Kc."