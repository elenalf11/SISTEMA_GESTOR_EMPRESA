numero = int(input("Dime un número y te diré su sumatorio: "))
suma = 0
for i in range(numero + 1):
    suma+=i
print("El sumatorio de ", numero, " es ", suma)