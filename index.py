nested_list = [
    [1, 2, [3, 4, [5, 6, 5], 5], 5],
    [7, 8, [5, 9, 5,5]],
    [10, [11, 5, 6], 12]
]

#pomocí indexování zvolte pole [5, 6, 5]
#pozn. indexování je např. nested_list[2][0]

# pomocí .count zjistěte, kolikrát se vyskytuje 5 v tomto poli.

vysledek = ...

#assert vysledek == 2, "Chybný výsledek"
#print("Gratuluji, správný výsledek")
#Code
prvy_sublist = nested_list[0]
druhy_sublist = prvy_sublist[2]
treti_sublist = druhy_sublist[2]
print(treti_sublist)
print(treti_sublist.count(5))
# ------------------------------------
index1 = nested_list.index([1, 2, [3, 4, [5, 6, 5], 5], 5])
level1 = nested_list[index1]

index2 = level1.index([3, 4, [5, 6, 5], 5])
level2 = level1[index2]

index3 = level2.index([5, 6, 5])
level3 = level2[index3]
print(level3)
print(level3.count(5))
