print("Kamen...")
print("Papier...")
print("Noznice...")
Dominik = input ("Dominik, tvoj tah: ").lower()
print("***NEPODVADZAT !!!***\n" * 20)
Viliam = input ("Viliam, tvoj tah: ").lower()
if Dominik == Viliam:
    print("Je to remiza !")
elif Dominik == "kamen":
    if Viliam == "papier":
        print("Viliam vyhrava !")
    elif Viliam == "noznice":
        print("Dominik vyhrava !")
elif Dominik == "papier":
    if Viliam == "kamen":
        print("Dominik vyhrava !")
    elif Viliam == "noznice":
        print("Viliam vyhrava !")
elif Dominik == "noznice":
    if Viliam == "kamen":
        print("Viliam vyhrava !")
    elif Viliam == "papier":
        print("Dominik vyhrava !")
else:
    print("Nieco sa pokazilo !")


