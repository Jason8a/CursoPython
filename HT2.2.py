
#datos
name = input("¿Cual es tu nombre? ")
gender = input("¿Cuál es tu genero M/F? ")
if gender == "F":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)