lista = []

while (True):
    num = int(input("Dime un número (0 si quieres salir): "))
    
    if (num == 0):
        break

    lista.append(num)


diccionario = {
    "pares" : [],
    "impares" : []
}

for i in lista:
    if(i % 2 == 0):
        diccionario["pares"].append(i)
    else:
        diccionario["impares"].append(i)

print(diccionario)