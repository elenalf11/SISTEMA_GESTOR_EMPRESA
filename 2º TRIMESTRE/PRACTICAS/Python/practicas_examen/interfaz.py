import tkinter as tk

def comprar():
    compra = tk.Toplevel()
    home.withdraw()
    compra.title("Aquí simulas tu compra")

    compra.config(bg = "lightblue")
    compra.geometry("700x500")

    title = tk.Label(
        compra,
        text = "Escribe aquí los datos para realizar la compra",
        bg = "lightblue",
        fg = "black",
        font = ("Arial", 15)
    )
    title.grid(row = 0, column = 0, pady = 10)

    category_text = tk.Label(
        compra,
        text = "Escribe aquí la categoría",
        bg = "lightblue",
        fg = "black",
        font = ("Arial", 15)
    )
    category_text.grid(row = 1, column = 0, pady = 10)

    category = tk.Entry(
        
    )


home = tk.Tk()
home.title("Práctica examen")

home.config(bg = "lightblue")
home.geometry("500x500")

title = tk.Label(
    home,
    text = "Esto es una ventana para prácticar el examen",
    bg = "lightblue",
    fg = "black",
    justify = "center",
    font = ("Arial", 15),
    anchor = "center"

)
title.grid(row = 0, column = 0, pady = 10, sticky = "nsew")

button_1 = tk.Button(
    home, 
    width = 12,
    height = 1,
    text = "Botón 1",
    bg = "lightpink",
    command = comprar
)
button_1.grid(row = 1, column = 0, pady = 10, padx = 10)

home.mainloop()