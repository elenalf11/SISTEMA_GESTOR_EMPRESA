lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumatorio = 0

for i in lista:
    if(i % 2 == 0):
        sumatorio += i
print(f"La suma de los números pares de la lista {lista} es {sumatorio}")