'''
Zadání:
Napiš program, který požádá uživatele o zadání čísla odpovídající přijmu firmy:

pokud je číslo kladné, tak se vypíše "Firma je v zisku"
pokud je číslo nula, tak se vypíše "Firma je na nule"
pokud je číslo záporné, tak se vypíše "Brzo bude krach"

'''
prijem = int(input("Aky bol Vas prijem?: "))
if prijem < 0:
	print("Brzo bude krach!")
elif prijem == 0:
	print("Firma je na nule.")
else:
	print("Firma je v zisku!")


