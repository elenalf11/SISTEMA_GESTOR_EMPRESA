def algoritmoLuhn(numero):
    suma = 0
    #Se invierte el número
    numero_invertido = numero[::-1]
    #Duplicar dígitos posiciones impares
    for i in range(0, len(numero_invertido), 3):
        numero_invertido[i] += i
    #Sumatorio de digitos
    for i in range(0, len(numero)):
        suma += int(numero_invertido[i])
    #Comprobación último dígito
    if(str(suma[-1]) == "0"):
        print("Es un número Luhn")
    else:
        print("No es un número Luhn")

numero = input("Dime un número: ")
algoritmoLuhn(numero)
