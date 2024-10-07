lista = [5, 2, 8, 5, 2, 1, 1, 1, 1, 1, 3, 5]
moda = None
max_contador = 0

for i in lista:
    contador = lista.count(i)
    if(contador > max_contador):
        max_contador = contador
        moda = i
print("La moda de la lista: ", lista, " es: ", moda)
