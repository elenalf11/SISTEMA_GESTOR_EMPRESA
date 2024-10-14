lista_1 = [1, 2, 3, 4, 5]
lista_2 = [5, 4, 7, 2, 1]

lista_ordenada_1 = sorted(lista_1)
lista_ordenada_2 = sorted(lista_2)

if(lista_ordenada_1 == lista_ordenada_2):
    print(f"Las listas {lista_1} {lista_2} tienen los mismos elementos")
else:
    print(f"Las listas {lista_1} {lista_2} no tienen los mismos elementos")