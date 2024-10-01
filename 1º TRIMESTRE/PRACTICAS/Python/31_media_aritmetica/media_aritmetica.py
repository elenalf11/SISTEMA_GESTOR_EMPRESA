lista = [1, 2, 3, 4, 5]
sumatorio = 0
longitud = len(lista)

for i in range(longitud):
    sumatorio += lista[i]
print("La media de ", lista, " es: ", sumatorio/longitud)
