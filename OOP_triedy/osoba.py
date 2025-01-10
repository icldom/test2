
#pamatat si pocet predmetov, kolko mame penazi, atd.
class Osoba:
	def __init__(self, name, lokace):
		self.name = name
		self.predmety = []
		self.peniaze = 100
		self.pocet_dnu = 0
		self.lokace = lokace

	def pohyb(self, nova_lokace):
		self.lokace = nova_lokace
		self.pocet_dnu += 1

	def koupit_predmet(self,predmet):
		self.predmety.append(predmet)
		self.peniaze -= predmet.current_price

	def predat_predmet(self,predmet):
		self.predmety.remove(predmet)
		self.peniaze += predmet.current_price

	def __str__(self):
		return f"{self.name} - Stav: {self.peniaze} Kc, Lokace: {self.lokace}, Ubehlo dni: {self.pocet_dnu}"

