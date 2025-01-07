'''
Zadání:
Napiš program, který požádá uživatele o zadání věku.
Program zkontroluje a vypíše, do které věkové kategorie patří:

"Dítě", pokud je věk menší než 12 let,
"Teenager", pokud je věk od 12 do 18 let,
"Dospělý", pokud je věk od 19 do 59 let,
"Senior", pokud je věk 60 a více let.
'''
age = int(input("Your age is?: "))

if age < 12:
	print("You are child.")
elif age >= 12 and age <= 18:
	print("You are already teenager.")
elif age >= 18 and age <= 59:
	print("You are already adult.")
else:
	print("You are senior.")
