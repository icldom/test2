text = "Pomocí speciálního příkazu s operátorem [] můžeme řetězec přečíst od konce?"
#znak "s"
print(f"Znak 's' sa vyskytuje; {text.count("s")}x")
#index 7 az 15 (including 7, excluding 15)
print(f"Na indexe 7 az 15 sa vyskytuju hodnoty; {text[7:15]}")
#slovo "operátorem"
print(f"Vysledek (slovo); {text[29:40]}")
#kazdy druhy znak
print(f"Kazdy druhy znak; {text[::2]}")
#text naopak
print(f"Text naopak; {text[::-1]}")





