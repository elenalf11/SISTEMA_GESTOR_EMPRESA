lista = [1, 2, 3, 4 , 1]

if(lista == lista[::-1]): #Comienza por el final
    print(f"La lista {lista} es palíndroma")
else:
    print(f"La lista {lista} no es palíndroma")