lista = [5, 7, 2, 9, 4, 8]

print(f"La lista original es {lista}")

for i in range (len(lista)):
    for j in range ((len(lista) - 1 - i)):
        if(lista[j] > lista [j + 1]):
            aux = lista[j + 1]
            lista[j + 1] = lista[j]
            lista[j] = aux

print(f"La lista ordenada es {lista}")
print(f"El segundo elemento mayor de la lista es el {lista[-2]}")