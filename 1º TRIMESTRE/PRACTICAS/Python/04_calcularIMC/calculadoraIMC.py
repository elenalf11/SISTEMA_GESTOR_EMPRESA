peso = float(input("Dime tu peso en kilogramos (Ej: 76): "))
altura = float(input("Dime tu altura en metros (Ej: 1.80): "))

imc = peso / (altura**2)

print("Tu IMC es de ", imc)