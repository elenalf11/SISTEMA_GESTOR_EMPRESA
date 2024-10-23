lista = [2, 0, 5, 7, 6, 0]
ceros = []

print(f"La lista original es {lista}")

for i in lista:
    if(i == 0):
        ceros.append(i)
        lista.remove(i)

lista.append(ceros)

print(f"La lista con los ceros al final es: {lista}")