zvirata = ["Pes", "Zajíc", "Pavouk", "Python", "Kočka", "Papoušek", "Pelikán"]
for zviratko in zvirata:
    if zviratko[0] != "P":
        continue
    print(zviratko)

soucet = 0
for i in range(10) : #range vygeneruje [0,1,2,3,4,5,6,7,8,9]
    soucet += i
    print(f"Číslo {i} a součet {soucet}")

print("Ukázka, že range(10) je to samé jako [0,1,2,3,4,5,6,7,8,9]")
for i in [0,1,2,3,4,5,6,7,8,9]: #stejné jako range(10)
    soucet += i
    print(f"Číslo {i} a součet {soucet}")

print("Ukázka range(5,10)")
for pocet_ropuch in range(5,10):
    print(f"Na silnici je {pocet_ropuch} ropuch")

print("Ukázka range(7,20,3)")
for telefony in range(7,20,3):
    print(f"Na prodej je {telefony} telefonů")