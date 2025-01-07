vsechny_jmena = ["Jura", ["Eliška", "Ruda"], "Božka", "Katka", ["Michal", "Liza"]] #Tento řádek neupravujte
#pomocí příkazu .remove(x) odeberte vsechny_jmena, tak aby obsahovala pouze:
# ["Jura", ["Eliška"], "Katka"]


#   ŘÁDKY níže neupravujte
assert jmena==vsechny_jmena, f"Chyba, vyšlo {vsechny_jmena}, ale mělo vyjít {jmena} "
print("Gratuluji")
vsechny_jmena[1].remove("Ruda")
vsechny_jmena.remove("Božka")
vsechny_jmena.remove(["Michal", "Liza"])
print(vsechny_jmena)
