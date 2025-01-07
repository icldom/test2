'''
Zadání:
Napiš program, který požádá uživatele o zadání čísla odpovídající známce (1 až 5). Program vypíše hodnocení:

1 = "Výborně"
2 = "Chvalitebně"
3 = "Dobře"
4 = "Dostatečně"
5 = "Nedostatečně"
Pokud uživatel zadá jiné číslo než 1–5, vypiš: "Neplatná známka".
'''
znamka = int(input("Aku znamku si dostal?: "))
if znamka == 1:
	print("Výborně")
elif znamka == 2:
	print("Chvalitebně")
elif znamka == 3:
	print("Dobře")
elif znamka == 4:
	print("Dostatečně")
elif znamka == 5:
	print("Nedostatečně")
else:
	print("Neplatna znamka!!!")






