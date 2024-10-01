lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = len(lista)
listaNueva = []

while(i >= 1):
    listaNueva.append(lista[i - 1])
    i-=1
print(listaNueva)