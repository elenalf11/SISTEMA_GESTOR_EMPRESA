lista_1 = []
lista_2 = []
end_1 = False
end_2 = False

print("Vamos a rellenar la lista 1")
while(end_1 == False):
    numero_1 = int(input("Dime un número, si no quieres añadir más números escribe -1: "))
    if(numero_1 != -1):
        lista_1.append(numero_1)
    else:
        end_1 = True

print("Vamos a rellenar la lista 2")
while(end_2 == False):
    numero_2 = int(input("Dime un número, si no quieres añadir más números escribe -1: "))
    if(numero_2 != -1):
        lista_2.append(numero_2)
    else:
        end_2 = True
print(f"La lista 1 es {lista_1} y la lista 2 es {lista_2}")

match lista_1:
    case lista_1 if(lista_1 == lista_2):
        print("Las 2 listas son exactamente iguales")
    case lista_1 if(sorted(lista_1) == sorted(lista_2)):
        print("Las 2 listan tienen los mismos elementos, pero están en diferente orden")
    case lista_1 if(len(lista_1) != len(lista_2)):
        print("Las 2 listas tienen diferentes tamaños")
    case lista_1 if(sorted(lista_1) != sorted(lista_2)):
        print("Las 2 listas no tienen elementos en común")