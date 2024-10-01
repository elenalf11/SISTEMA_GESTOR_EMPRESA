dividendo = int(input("¿Qué número quieres dividir?: "))
divisor = int(input("¿Por qué número quieres dividirlo?: "))
cociente = 0
i = dividendo


while(i > 0):
    i -= divisor
    cociente += 1

print("El dividendo es ", dividendo, ", el divisor es ", divisor, ", el cociente es ", cociente, " y el resto es ", i)