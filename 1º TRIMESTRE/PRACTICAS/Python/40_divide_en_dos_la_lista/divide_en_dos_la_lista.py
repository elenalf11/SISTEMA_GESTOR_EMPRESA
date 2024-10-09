numero = int(input("Dime un número: "))
lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = []

for i in range (len(lista_1)):
    if(numero > lista_1[i]):
        lista_2.append(lista_1[i])
 
    else:
        pass
print("La lista con números mayores a ", numero, " es: ", lista_1, " y la de números menores: ", lista_2)