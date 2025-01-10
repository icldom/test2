
#v lokalite su ulozene predmety
class Lokace:
	def __init__(self, nazev_lokace, utopenec, med, lahev_palavy):
		self.nazev_lokace = nazev_lokace
		self.utopenec = utopenec
		self.med = med
		self.lahev_palavy = lahev_palavy

	def __str__(self):
		return f"{self.nazev_lokace}"