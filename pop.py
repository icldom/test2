vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .pop(index) odeberte vsechny_jmena, tak aby obsahovala pouze:
# ["Jura", ["Eliška"], "Katka"]


#   ŘÁDKY níže neupravujte
#assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")
#Code
vsechny_jmena[1].pop(1)
vsechny_jmena.pop(2)
vsechny_jmena.pop(3)
print(vsechny_jmena)

