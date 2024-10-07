lista = [5, 2, 8, 9, 4, 6]
print("La lista desordenada es: ", lista)

for i in range (len(lista)):
    for j in range(len(lista) - 1 - i):
        if(lista[j] > lista[j + 1]):
            aux = lista[j + 1]
            lista[j + 1] = lista[j]
            lista[j] = aux
print("La lista ordenada es: ", lista)