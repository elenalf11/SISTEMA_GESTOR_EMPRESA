import random

numero_secreto = random.randint(1, 10)
intentos = 0

print("¡Adivina el númreo secreto entre 1 y 100")
while True:
    intento = int(input("Dime un número: "))
    intentos += 1

    if(intento == numero_secreto):
        print("¡Enhorabuena, adivinaste el numero en ", intentos, " intentos")
        break
    elif(intento < numero_secreto):
        print("Demasiado bajo. Intenta de nuevo")
    else:
        print("Demasiado alto. Intenta de nuevo")
    
