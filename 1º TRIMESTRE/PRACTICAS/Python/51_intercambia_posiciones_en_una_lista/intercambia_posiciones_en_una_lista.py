lista = [1, 2, 3, 4, 5]

print(f"La lista original es {lista}")

aux = lista[0]
lista[0] = lista[-1]
lista[-1] = aux

print(f"La lista modificada es {lista}")