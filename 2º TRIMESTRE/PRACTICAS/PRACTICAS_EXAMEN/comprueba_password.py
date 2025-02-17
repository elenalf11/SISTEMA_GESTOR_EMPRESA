import tkinter as tk
import re

letras = re.compile(r'[a-zA-Z]')
numeros = re.compile(r'[0-9]')
caracteres = re.compile(r'[ªº\!|"@·#$€%&¬/()=?¿¡^`*+]')

def comprobar_password():
    global letras, numeros, caracteres
    cadena = entrada.get()

    if(len(cadena) >= 8):
        if(letras.search(cadena)):
            if(numeros.search(cadena)):
                if(caracteres.search(cadena)):
                    resultado.config(text = "¡Enhorabuena! La contraseña es segura")
                else:
                    resultado.config(text = "La contraseña no es segura, no contiene caracteres especiales")
            else:
                resultado.config(text = "La contraseña no es segura, no tiene números")
        else:
            resultado.config(text = "La contraseña no es segura, no tiene letras mayúsculas ni minúsculas")
    else:
        resultado.config(text = "La contraseña no es segura, no cumple con el tamaño mínimo")

ventana = tk.Tk()
ventana.title("Comprueba tu contraseña")
ventana.geometry("500x500")

text = tk.Label(ventana, text="Escribe aquí tu contraseña: ")
text.grid(row = 0, column = 0, pady = 10)

entrada = tk.Entry(ventana)
entrada.grid(row = 0, column = 1, pady = 10, padx = 10)

boton = tk.Button(ventana, text = "Comprobar", command=comprobar_password)
boton.grid(row = 1, column = 0, pady = 10, padx = 10)

resultado = tk.Label(ventana, text = "Resultado: ")
resultado.grid(row = 2, column = 0, pady = 10, padx = 10)

ventana.mainloop()