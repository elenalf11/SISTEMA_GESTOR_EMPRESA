import tkinter as tk

def diaSemana():
    try:
        num = int(entrada.get())
        match num:
            case 1:
                resultado.config(text = "Es lunes")
            case 2:
                resultado.config(text = "Es martes")
            case 3:
                resultado.config(text = "Es miércoles")
            case 4:
                resultado.config(text = "Es jueves")
            case 5:
                resultado.config(text = "Es viernes")
            case 6:
                resultado.config(text = "Es sábado")
            case 7:
                resultado.config(text = "Es domingo")
            case _:
                resultado.config(text = "Ese día no existe")
    except ValueError:
        resultado.config(text ="¡Solo números válidos!")
    
    

# Crear ventana
ventana = tk.Tk()
ventana.title("Días de la semana")

# Crear entradas
entrada = tk.Entry(ventana)
entrada.grid(row=0, column=0, padx=10, pady=10)

# Crear botón
boton = tk.Button(ventana, text = "Comprobar", command = diaSemana)
boton.grid(row=1, column=0, pady=10)

# Crear etiqueta para mostar el resultado
resultado = tk.Label(ventana, text = "Resultado: ")
resultado.grid(row=2, column=0, pady=10)

# Iniciar bucle para la ventana
ventana.mainloop()