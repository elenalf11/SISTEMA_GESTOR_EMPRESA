lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0

for i in range (len(lista)):
    if(lista[i] % 2 == 0):
        pares += 1
    else:
        impares += 1
print("En la lista: ", lista, " hay ", pares, " números pares y ", impares, " números impares")
