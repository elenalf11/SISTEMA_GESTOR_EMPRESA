import tkinter as tk

ventana = tk.Tk()
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

ventana.mainloop()