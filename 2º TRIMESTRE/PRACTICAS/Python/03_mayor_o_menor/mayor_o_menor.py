import tkinter as tk

def mayorOmenor():
    try:
        num1 = int(entrada1.get())
        num2 = int(entrada2.get())
        if(num1 > num2):
            resultado.config(text = f"El número {num1} > {num2}")
        elif (num2 > num1):
            resultado.config(text = f"El número {num2} > {num1}")
        else:
            resultado.config(text = f"El número {num1} = {num2}")
    except ValueError:
        resultado.config("¡Ingrese un número válido!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("¿Qué número es mayor?")

# Crear cuadros de entrada
entrada1 = tk.Entry(ventana)
entrada1.grid(row = 0, column = 0, rowspan = 10, pady = 0)

entrada2 = tk.Entry(ventana)
entrada2.grid(row = 0, column = 1, rowspan = 10, pady = 0)

# Boton para activar la función
boton = tk.Button(ventana, text = "Comprobar", command = mayorOmenor)
boton.grid(row = 1, column = 0,  columnspan = 10, pady = 10)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text = "Resultado: ")
resultado.grid(row = 2, column = 0, columnspan = 10, pady = 10)

# Iniciar el bucle de la ventana
ventana.mainloop()