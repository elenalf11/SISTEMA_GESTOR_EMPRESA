lista_1 = [1, 2, 3, 4]
lista_2 = [5, 6, 7, 8, 9, 10]

tupla = ()

while ((len(lista_1) < len(lista_2)) or (len(lista_1) > len(lista_2))):
    if(len(lista_1) < len(lista_2)):
        lista_1.append(None)
    elif(len(lista_1) > len(lista_2)):
        lista_2.append(None)

tupla = lista_1 + lista_2
print(f"La tupla final es: {tupla}")