import tkinter as tk

def suma (num1, num2):


calculadora = tk.Tk()
calculadora.title("Calculadora final")

calculadora.config(bg = "lightblue")
calculadora.geometry("400x700")

result = tk.Label(
    calculadora, 
    text = "",
    bg = "lightblue",
)
result.grid(row = 0, column = 0, columnspan = 3, pady = 10)

num_1 = tk.Button(
    calculadora, 
    text = "1",
    width = 5,
    height = 2,
    command = 1,
    bg = "lightpink"
)
num_1.grid(row = 1, column = 0, pady = 10, padx = 10)

num_2 = tk.Button(
    calculadora, 
    text = "2",
    width = 5,
    height = 2,
    command = 2,
    bg = "lightpink"
)
num_2.grid(row = 1, column = 1, pady = 10, padx = 10)

num_3 = tk.Button(
    calculadora, 
    text = "3",
    width = 5,
    height = 2,
    command = 3,
    bg = "lightpink"
)
num_3.grid(row = 1, column = 2, pady = 10, padx = 10)

num_4 = tk.Button(
    calculadora, 
    text = "4",
    width = 5,
    height = 2,
    command = 4,
    bg = "lightpink"
)
num_4.grid(row = 2, column = 0, pady = 10, padx = 10)

num_5 = tk.Button(
    calculadora, 
    text = "5",
    width = 5,
    height = 2,
    command = 5,
    bg = "lightpink"
)
num_5.grid(row = 2, column = 1, pady = 10, padx = 10)

num_6 = tk.Button(
    calculadora, 
    text = "6",
    width = 5,
    height = 2,
    command = 6,
    bg = "lightpink"
)
num_6.grid(row = 2, column = 2, pady = 10, padx = 10)

num_7 = tk.Button(
    calculadora, 
    text = "7",
    width = 5,
    height = 2,
    command = 7,
    bg = "lightpink"
)
num_7.grid(row = 3, column = 0, pady = 10, padx = 10)

num_8 = tk.Button(
    calculadora, 
    text = "8",
    width = 5,
    height = 2,
    command = 8,
    bg = "lightpink"
)
num_8.grid(row = 3, column = 1, pady = 10, padx = 10)

num_9 = tk.Button(
    calculadora, 
    text = "9",
    width = 5,
    height = 2,
    command = 9,
    bg = "lightpink"
)
num_9.grid(row = 3, column = 2, pady = 10, padx = 10)

num_0 = tk.Button(
    calculadora, 
    text = "0",
    width = 5,
    height = 2,
    command = 0,
    bg = "lightpink"
)
num_0.grid(row = 4, column = 0, columnspan= 2, pady = 10, padx = 10)

num_suma = tk.Button(
    calculadora, 
    text = "+",
    width = 5,
    height = 2,
    command = suma,
    bg = "lightpink"
)

num_resta = tk.Button(
    calculadora,
    text = "-",
    width = 5,
    height = 2,
    command = resta,
    bg = "lightpink"
)

num_multiplicacion = tk.Button(
    calculadora,
    text = "X",
    width = 5,
    height = 2,
    command = multiplicacion,
    bg = "lightpink"
)

num_division = tk.Button(
    calculadora,
    text = "/",
    width = 5,
    height = 2,
    command = division,
    bg = "lightpink"
)
calculadora.mainloop()