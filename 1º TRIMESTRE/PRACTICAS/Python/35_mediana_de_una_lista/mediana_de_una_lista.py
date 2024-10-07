lista = [5, 2, 1, 4, 9, 8, 3]
longitud = len(lista)
mediana_impar = lista[longitud//2]

if(longitud % 2 == 0):
    num_par_1 = lista[longitud//2]
    num_par_2 = lista[longitud//2 - 1]
    mediana_par = (num_par_1 + num_par_2)/2
    print("La mediana de la lista: ", lista, " es la media aritmética entre: ", num_par_1, num_par_2, " es: ", mediana_par)
else:
    print("La mediana de la lista: ", lista, " es: ", mediana_impar)

