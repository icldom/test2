#Vytvořte třídu Položka. Třída Položka má atributy název a cena.
class Polozka:
    pass

maslo = Polozka("Máslo", 80)
chipsy = Polozka("Chilli&Lime", 34)
propiska = Polozka("Propiska", 45)

#Vytvořte třídu Košík. Košík má atribut položky (list).
#Košík má metodu pridat_polozku. Košík má metodu vypsat_polozky.
class Kosik:
    pass

katka = Kosik()
katka.pridat_polozku(maslo)
katka.pridat_polozku(chipsy)
katka.pridat_polozku(chipsy)
katka.vypsat_polozky() # V košíku je Máslo, Chilli&Lime, Chilli&Lime. Celková cena 148 Kč
#Extra: # V košíku je 1x: Máslo, 2x: Chilli&Lime. Celková cena 148 Kč

pavel = Kosik()
pavel.pridat_polozku(propiska)
pavel.pridat_polozku(maslo)
pavel.pridat_polozku(chipsy)
pavel.vypsat_polozky() # V košíku je Propiska, Máslo, Chilli&Lime. Celková cena 159 Kč