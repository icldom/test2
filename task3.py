text = input("Zadejte text: ")
if text.islower():
    print(True)
elif text.isupper():
    print(False)
else:
    print("Error")