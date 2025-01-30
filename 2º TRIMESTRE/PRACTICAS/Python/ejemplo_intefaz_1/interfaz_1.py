import tkinter as tk
from tkinter import messagebox

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera interfaz gráfica")

#Función que se ejecuta al hacer clic en el botón
def saludar():
    messagebox.showinfo("Saludo", "¡Hola mundo!")

#Crear un botón
boton = tk.Button(ventana, text="Saludar", command = saludar)
boton.pack(pady = 20)

def mostrar_opcion():
    print(f"Opción seleccionada: {radio_var.get()}")

radio_var = tk.StringVar(value="Opción 1")
radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=radio_var, value="Opción 1", command=mostrar_opcion)
radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=radio_var, value="Opción 2", command=mostrar_opcion)
radio1.pack()
radio2.pack()

def mostrar_seleccion_lista():
    seleccion = lista.curselection()
    if seleccion:
        print(f"Seleccionaste: {lista.get(seleccion)}")

lista = tk.Listbox(ventana)
lista.insert(1, "Opción 1")
lista.insert(2, "Opción 2")
lista.insert(3, "Opción 3")
lista.pack(pady=10)

boton_lista = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion_lista)
boton_lista.pack()

def mostrar_seleccion():
    if check_var.get() == 1:
        print("Casilla marcada")
    else:
        print("Casilla desmarcada")

check_var = tk.IntVar()
check = tk.Checkbutton(ventana, text="Acepto los términos", variable=check_var, command=mostrar_seleccion)
check.pack(pady=10)

#Iniciar el bucle principal de la ventana
ventana.mainloop()