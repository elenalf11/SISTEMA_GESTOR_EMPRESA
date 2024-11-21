import random


precio = random.randint(11, 93)

billete = int(input(f"El precio es {precio} €, ¿cuánto me vas a pagar?: "))

resta = (billete - precio)

while(resta > 0):
    if(resta >= 100):
        print("Te devuelvo 100 €")
        resta -= 100
    elif (resta >= 50):
        print("Te devuelvo 50 €")
        resta -=50
    elif(resta >= 20):
        print("Te devuelvo 20 €")
        resta -= 20
    elif(resta >= 10):
        print("Te devuelvo 10 €")
        resta -= 10
    elif(resta >= 5):
        print("Te devuelvo 5 €")
        resta -= 5
    elif(resta >= 2):
        print("Te devuelvo 2 €")
        resta -= 2
    elif (resta >= 1):
        print("Te devuelvo 1 €")
        resta -=1