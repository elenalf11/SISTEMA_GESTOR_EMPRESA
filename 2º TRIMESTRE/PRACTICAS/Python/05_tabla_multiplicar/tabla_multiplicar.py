import tkinter as tk

def tablaMultiplicar():
    try:
        num = int(entrada.get())
        texto = ""
        for i in range (1, 11):
            texto += f"{num} * {i} = {num * i} \n"
        resultado.config(text = texto)
    except ValueError:
        resultado.config(text = "¡Solo números válidos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Tablas de multiplicar")

# Crear entradas
entrada = tk.Entry(ventana)
entrada.grid(row=0, column=0, padx=10, pady=10)

# Crear botón
boton = tk.Button(ventana, text = "Comprobar", command = tablaMultiplicar)
boton.grid(row=1, column=0, pady=10)

# Crear etiqueta para mostar el resultado
resultado = tk.Label(ventana, text = "Resultado: ")
resultado.grid(row=2, column=0, pady=10)

# Iniciar bucle para la ventana
ventana.mainloop()