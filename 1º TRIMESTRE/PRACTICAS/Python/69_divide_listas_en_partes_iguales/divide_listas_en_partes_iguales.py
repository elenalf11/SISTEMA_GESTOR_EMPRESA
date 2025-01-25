lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num = int(input(f"Dime en cuántas partes quieres dividir la lista {lista}: "))

if(len(lista) % num == 0):
    lista_nueva = []
    lista_original = []
    for i in range(len(lista)//num):
        lista_nueva.append(lista[i])
    for i in range(len(lista)//num, len(lista)):
        lista_original.append(lista[i])

    
    print(f"Lista 1: {lista_nueva} \nLista 2: {lista_original}")