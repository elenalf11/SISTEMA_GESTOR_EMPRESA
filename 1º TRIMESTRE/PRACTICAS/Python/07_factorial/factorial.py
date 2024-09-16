numero = int(input("Dime un número y te calculo su factorial: "))
factorial = 1

for i in range(numero, 1, -1):
    factorial *= i

print("El factorial de ", numero, " es ", factorial)