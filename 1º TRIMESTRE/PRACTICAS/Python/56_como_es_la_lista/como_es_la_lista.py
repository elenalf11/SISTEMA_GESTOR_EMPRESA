lista_1 = [5, 4, 3, 2, 1]
lista_2 = [3]
lista_3 = []

size = len(lista_1)

match size:
    case 0:
        print("La lista está vacía")
    case 1:
        print("La lista sólo tiene un elemento")
    case _:
        print(f"La lista tiene {size} elementos" )
