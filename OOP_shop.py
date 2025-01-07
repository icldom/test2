
#Create class "item". Class "item" has attributes name and prize.
class Item: #trieda
	def __init__(self,name,prize,): #metoda + #parametre
		self.name = name #attributes
		self.prize = prize #attribtues
	pass
butter = Item("butter", 2.25)
chips = Item("chips", 1.55)
bread = Item("bread", 2)

#Class "basket". Basket has attribute items [list].
#Basket has method "add item". Basket has method "write down content".

class Basket:
	def __init__(self):
		self.content = []
	pass

	def add_item(self,item):
		self.content.append(item)
		print(f"In the basket is {item.name} that costs {item.prize}€ .")
	pass

	def write_down(self):
		for item in self.content:
			print(f"In the basket is {item.name} that costs {item.prize}€ .")
	pass
katka = Basket()
katka.add_item(butter)
katka.add_item(bread)
katka.add_item(chips)
katka.write_down() #Writedown - "In the basket is butter, chipsy and bread."




