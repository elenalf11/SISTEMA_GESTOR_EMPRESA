import tkinter as tk
import random as r

vidas = 4
numero = r.randint(0, 100)

def adivinar():
    global vidas, numero
    tuNum = int(entrada.get())
    try:
        if(vidas > 0):
            if(tuNum == numero):
                resultado.config(text = f"¡Enhorabuena! Has adivinado el número, lo has conseguido con un total de {vidas} vidas")
            elif (tuNum < numero):
                resultado.config(text = f"Tu número es demasiado pequeño, inténtalo de nuevo, te quedan {vidas} vidas")
                vidas -= 1
            elif (tuNum > numero):
                resultado.config(text = f"Tu número es demasiado alto, inténtalo de nuevo, te quedan {vidas} vidas")
                vidas -= 1
        else:
            resultado.config(text = f"Lo siento has perdido, el número era {numero}")
    except ValueError:
        resultado.config(text = "Por favor, ingrese números válidos")
        
ventana = tk.Tk()
ventana.title("Adivina el número")
ventana.geometry("500x300")

texto = tk.Label(ventana, text = "Escribe aquí tu número")
texto.grid(row = 0, column = 0, pady = 10)

entrada = tk.Entry(ventana)
entrada.grid(row = 0, column = 1, pady = 10, padx = 10)

boton = tk.Button(ventana, text = "Comprobar", command = adivinar)
boton.grid(row = 1, column = 0, pady = 10, padx = 10)

resultado = tk.Label(ventana, text = "Resultado: ")
resultado.grid(row = 2, column = 0, pady = 10)

ventana.mainloop()