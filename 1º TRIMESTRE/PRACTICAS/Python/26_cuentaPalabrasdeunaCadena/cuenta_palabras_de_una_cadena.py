cadena = input("Dime una cadena de palabras: ")
palabras = cadena.split()
numero = 0
for i in palabras:
    numero += 1
print("La cadena tiene ", numero, " palabras")