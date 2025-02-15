import tkinter as tk


def juego(num:int):
    tuNum = int(num)
    numero = 17
    vidas = 4
    terminado = False
    while (vidas > 0 and not terminado):
        if(tuNum == numero):
            #resultado.config(f"¡Enhorabuena has acertado el número, el número es {numero} y te han quedado {vidas} vidas")
            print(f"¡Enhorabuena has acertado el número, el número es {numero} y te han quedado {vidas} vidas")
            resultado = True
            return
        elif (tuNum < numero):
            #resultado.config(f"El número es más grande. Acabas de perder una vida")
            print(f"El número es más grande. Acabas de perder una vida")
            vidas -= 1
        elif (tuNum > numero):
            #resultado.config(f"El número es más pequeño. Acabas de perder una vida")
            print(f"El número es más pequeño. Acabas de perder una vida")
            vidas -= 1
        tuNum = int(input("Prueba con otro número: "))

num = int(input("Dime un número: "))
juego(num)


