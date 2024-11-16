num = int(input("Dime un número y lo agregamos al array (si no quieres añadir más escribe -1): "))
lista = []
sumatorio = 0

while(num > 0):
    lista.append(num)
    num = int(input("Dime un número y lo agregamos al array (si no quieres añadir más escribe -1): "))

for i in lista:
    sumatorio += i

print(f"La suma del array: {lista} es {sumatorio}")