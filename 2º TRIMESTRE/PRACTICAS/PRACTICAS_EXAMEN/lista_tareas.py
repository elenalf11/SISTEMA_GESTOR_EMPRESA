import tkinter as tk

tareas = []

def addTarea():
    global tareas
    tarea = entrada.get()
    if(tarea != ""):
        tareas.append(tarea)
        tareas_texto.config(text = "\n".join(tareas))
        entrada.delete(0, tk.END)

def eliminarTarea():
    global tareas
    tareas.pop()
    tareas_texto.config(text = "\n".join(tareas))
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("500x500")

entrada = tk.Entry(ventana)
entrada.grid(row = 0, column = 0, pady = 10, padx = 10)

boton = tk.Button(ventana, text = "Añadir tarea", command = lambda : addTarea())
boton.grid(row = 0, column = 1, pady = 10, padx = 10)

boton_eliminar = tk.Button(ventana, text = "Eliminar tarea", command = lambda: eliminarTarea())
boton_eliminar.grid(row = 0, column = 2, pady = 10, padx = 10)

tareas_texto = tk.Label(ventana, text = "Aquí aparecerán todas tus tareas")
tareas_texto.grid(row = 1, column = 0, pady = 10, padx = 10)

ventana.mainloop()