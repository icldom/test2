#Vytvořte třídu Položka. Třída Položka má atributy název a cena.
class Polozka:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def __repr__(self):
        return f"{self.nazev} - {self.cena} Kč"

maslo = Polozka("Máslo", 80)
chipsy = Polozka("Chilli&Lime", 34)
propiska = Polozka("Propiska", 45)

#Vytvořte třídu Košík. Košík má atribut položky (list).
#Košík má metodu pridat_polozku. Košík má metodu vypsat_polozky.
class Kosik:
    def __init__(self):
        self.polozky : list[Polozka] = []

    def pridat_polozku(self, polozka : Polozka):
        self.polozky.append(polozka)
        #print(f"Přidali jste item {item.nazev} do košíku")

    def vypsat_polozky(self):
        celkova_cena = 0
        print("V košíku je ", end='')
        pocty_polozek = {} #klíč bude název položky, hodnota bude počet
        for polozka in self.polozky:
            #print(f"{polozka.nazev}, ", end='')
            celkova_cena += polozka.cena
            pocty_polozek[polozka.nazev] = 0
        pass
        for polozka in self.polozky:
            pocty_polozek[polozka.nazev] += 1 # pokud položka již v dict je
        for key, value in pocty_polozek.items():
            print(f"Položka {key} je v košíku {value} krát")

        print(f"Celková cena je {celkova_cena} Kč. Celkem je položek {len(self.polozky)}")

katka = Kosik()
katka.pridat_polozku(maslo)
katka.pridat_polozku(chipsy)
katka.pridat_polozku(chipsy)
katka.pridat_polozku(chipsy)
katka.vypsat_polozky() # V košíku je Máslo, Chilli&Lime, Chilli&Lime. Celková cena 148 Kč
#Extra: # V košíku je 1x: Máslo, 2x: Chilli&Lime. Celková cena 148 Kč

pavel = Kosik()
pavel.pridat_polozku(propiska)
pavel.pridat_polozku(maslo)
pavel.pridat_polozku(chipsy)
pavel.vypsat_polozky() # V košíku je Propiska, Máslo, Chilli&Lime. Celková cena 159 Kč