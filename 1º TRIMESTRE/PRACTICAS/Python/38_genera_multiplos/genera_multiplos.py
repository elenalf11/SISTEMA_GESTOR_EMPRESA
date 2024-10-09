numero = int(input("Dime un número y te diré sus múltiplos: "))
cantidad = int(input("¿Cuántos quieres que te muestre?: "))

for i in range (cantidad):
    print(numero, ": ", numero*i)
