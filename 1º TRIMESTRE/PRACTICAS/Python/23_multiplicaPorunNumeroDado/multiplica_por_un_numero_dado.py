lista = [2, 5, 4, 9, 4, 3]
numero = int(input("Dime un número: "))
nueva_lista = []
for i in lista:
    nueva_lista.append(i * numero)
print("La lista original es: ", lista)
print("La lista multiplicada por ", numero, " es ", nueva_lista)