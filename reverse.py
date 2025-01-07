puvodni_list = [1,4,9,[5,2],6] #Nesahat na toto
# Použijte dva příkazy .reverse() tak ať dostanete: [6, [2, 5], 9, 4, 1]

#Na řádky níže nesahat
#assert puvodni_list == [6, [2, 5], 9, 4, 1], f"Chyba, má vyjít [6, [2, 5], 9, 4, 1], ale vyšlo {puvodni_list}"
print("Správně!!")
#Code
puvodni_list.reverse()
puvodni_list[1].reverse()
print(puvodni_list)


