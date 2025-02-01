import tkinter as tk

# Función para ver si es el número es par o impar
def esPar():
    try:
        num1 = int(entrada.get())
        if(num1 % 2 == 0):
            resultado.config(text = f"El número {num1} es par")
        else:
            resultado.config(text = f"El número {num1} es impar")
    except ValueError:
        resultado.config(text = "¡Ingresa un número válido!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Comprueba pares")

# Crear cuadros de entrada
entrada = tk.Entry(ventana)
entrada.grid(row = 0, column = 0, padx = 10, pady = 0)

# Boton para activar la funcion
boton = tk.Button(ventana, text = "Comprobar", command = esPar)
boton.grid(row = 1, column = 0, columnspan = 2, pady = 10 )

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text = "Resultado: ")
resultado.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar el bucle para mostrar la ventana
ventana.mainloop()