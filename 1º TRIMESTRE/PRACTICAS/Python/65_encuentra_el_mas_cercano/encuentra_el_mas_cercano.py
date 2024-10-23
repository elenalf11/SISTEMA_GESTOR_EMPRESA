lista = [2, 5, 7, 3, 0, 4]

num = int(input("Dime un número: "))

for i in lista:
    if(i == num):
        print(f"Tu número ha sido encontrado en la lista, tu número es {i}")
    elif (i == num + 1):
        print(f"Tu número no ha sido encontrado en la lista, el más cercano es {i}")
    elif (i == num - 1):
         print(f"Tu número no ha sido encontrado en la lista, el más cercano es {i}")
    else:
        print("Demasiado alto o bajo")
        break