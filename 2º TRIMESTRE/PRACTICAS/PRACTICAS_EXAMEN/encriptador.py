import tkinter as tk

def encriptar():
    cadena = entrada.get()
    newCadena = ""
    diccionario = {
        "A" : "4",
        "B" : "8",
        "C" : ")",
        "D" : "$",
        "E" : "3",
        "F" : "7",
        "G" : "?",
        "H" : "+",
        "I" : "1",
        "J" : "|",
        "K" : "&",
        "L" : "¬",
        "M" : "{",
        "N" : "2",
        "O" : "0",
        "P" : "6",
        "Q" : "¿",
        "R" : "%",
        "S" : "5",
        "T" : "¡",
        "V" : "<",
        "W" : "=",
        "X" : "*",
        "Y" : "#",
        "Z" : "\!",
        " " : "_"
    }

    for i in range(0, len(cadena)):
        newCadena += diccionario.get(cadena[i].upper())
    
    resultado.config(text = newCadena)

def desencriptar():
    cadena = resultado.cget("text")
    newCadena = ""
    diccionario = {
        "4" : "A",
        "8" : "B",
        ")" : "C",
        "$" : "D",
        "3" : "E",
        "7" : "F",
        "?" : "G",
        "+" : "H",
        "1" : "I",
        "|" : "J",
        "&" : "K",
        "¬" : "L",
        "{" : "M",
        "2" : "N",
        "0" : "O",
        "6" : "P",
        "¿" : "Q",
        "%" : "R",
        "5" : "S",
        "¡" : "T",
        "<" : "V",
        "=" : "W",
        "*" : "X",
        "#" : "Y",
        "\!" : "Z",
        "_" : " "
    }
     
    for i in range(0, len(cadena)):
        newCadena += diccionario.get(cadena[i])
    
    resultado.config(text = newCadena)



ventana = tk.Tk()
ventana.title("Encriptador de mensajes")
ventana.geometry("500x500")

texto = tk.Label(ventana, text = "Escribe aquí tu mensaje")
texto.grid(row = 0, column = 0, pady = 10)

entrada = tk.Entry(ventana)
entrada.grid(row = 0, column = 1, pady = 10, padx = 10)

boton_1 = tk.Button(ventana, text = "Encriptar", command=encriptar)
boton_1.grid(row = 1, column = 0, pady = 10, padx = 10)

boton_2 = tk.Button(ventana, text = "Desencriptar", command=desencriptar)
boton_2.grid(row = 1, column = 1, pady = 10, padx = 10)

resultado = tk.Label(ventana, text = "Resultado: ")
resultado.grid(row = 2, column = 0, pady = 10)

ventana.mainloop()

