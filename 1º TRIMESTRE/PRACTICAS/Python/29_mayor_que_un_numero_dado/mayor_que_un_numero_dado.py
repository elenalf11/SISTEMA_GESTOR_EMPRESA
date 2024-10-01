lista = [1, 19, 3, 4, 4, 12, 7, 18, 9, 9, 11, 4, 13, 13, 14, 15, 16, 17, 8, 2]
numero = int(input("Dime un número: "))
ordenada = sorted(lista)
listaNueva = []


i = 0
while(i < len(ordenada)):
    if(numero >= ordenada[i]):
        listaNueva.append(ordenada[i])
    i+=1
print(listaNueva)
