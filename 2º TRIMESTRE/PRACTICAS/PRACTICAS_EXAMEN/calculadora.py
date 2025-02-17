import tkinter as tk

i = 0

def click_boton(valor):
    global i
    display.insert(i, valor)
    i += 1

def borrar():
    display.delete(0, tk.END)
    i = 0

def resultado():
    operacion = display.get()
    resultado = eval(operacion)
    display.delete(0, tk.END)
    display.insert(1, resultado)

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("600x600")

# Display Calculadora
display = tk.Entry(ventana)
display.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx = 10)

# Primera fila botones
boton_7 = tk.Button(ventana, text = "7", command = lambda: click_boton(7))
boton_7.grid(row = 1, column = 0, pady = 10, padx = 10)
boton_8 = tk.Button(ventana, text = "8", command = lambda: click_boton(8))
boton_8.grid(row = 1, column = 1, pady = 10, padx = 10)
boton_9 = tk.Button(ventana, text = "9", command = lambda: click_boton(9))
boton_9.grid(row = 1, column = 2, pady = 10, padx = 10)
boton_division = tk.Button(ventana, text = "/", command = lambda: click_boton("/"))
boton_division.grid(row = 1, column = 3, pady = 10, padx = 10)

# Segunda fila botones
boton_4 = tk.Button(ventana, text = "4", command = lambda: click_boton(4))
boton_4.grid(row = 2, column = 0, pady = 10, padx = 10)
boton_5 = tk.Button(ventana, text = "5", command = lambda: click_boton(5))
boton_5.grid(row = 2, column = 1, pady = 10, padx = 10)
boton_6 = tk.Button(ventana, text = "6", command = lambda: click_boton(6))
boton_6.grid(row = 2, column = 2, pady = 10, padx = 10)
boton_multiplicar = tk.Button(ventana, text = "*", command = lambda: click_boton("*"))
boton_multiplicar.grid(row = 2, column = 3, pady = 10, padx = 10)

# Tercera fila botones
boton_1 = tk.Button(ventana, text = "1", command = lambda: click_boton(1))
boton_1.grid(row = 3, column = 0, pady = 10, padx = 10)
boton_2 = tk.Button(ventana, text = "2", command = lambda: click_boton(2))
boton_2.grid(row = 3, column = 1, pady = 10, padx = 10)
boton_3 = tk.Button(ventana, text = "3", command = lambda: click_boton(3))
boton_3.grid(row = 3, column = 2, pady = 10, padx = 10)
boton_resta = tk.Button(ventana, text = "-", command = lambda: click_boton("-"))
boton_resta.grid(row = 3, column = 3, pady = 10, padx = 10)

# Cuarta fila botones
boton_0 = tk.Button(ventana, text = "0", command = lambda: click_boton(0))
boton_0.grid(row = 4, column = 0, pady = 10, padx = 10)
boton_borrar = tk.Button(ventana, text = "AC", command = lambda : borrar())
boton_borrar.grid(row = 4, column = 1, pady = 10, padx = 10)
boton_suma = tk.Button(ventana, text = "+", command = lambda: click_boton("+"))
boton_suma.grid(row = 4, column = 2, pady = 10, padx = 10)
boton_igual = tk.Button(ventana, text = "=", command = lambda: resultado())
boton_igual.grid(row = 4, column = 3, pady = 10, padx = 10)

ventana.mainloop()