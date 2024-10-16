lista = []
end = False

print("Vamos a rellenar la lista")
while(end == False):
    num = int(input("Dime un número, si no quieres añadir más, escribe -1: "))
    if(num != -1):
        lista.append(num)
    else:
        end = True
print(f"La lista es {lista}")

match lista:
    case lista if(len(lista) == 0):
        print("La lista está vacía")
    case lista if(sorted(lista)[0] < 0 or sorted(lista)[-1] < 0):
        print("La lista solo tiene números negativos")
    case lista if(sorted(lista)[0] > 0):
        print("La lista solo tiene números positivos")
    case lista if(sorted(lista)[0] < 0 and sorted(lista)[-1] > 0):
        print("La lista tiene una mezcla de números positivos y negativos")
    case _:
        print("La lista tiene numeros y otros elementos")
