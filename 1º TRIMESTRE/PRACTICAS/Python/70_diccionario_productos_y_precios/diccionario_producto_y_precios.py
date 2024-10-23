diccionario = {"tomate":2, 
               "patatas":1, 
               "tv":200, 
               "pc":1000, 
               "movil":300
}

usuario = input("Dime un elemento que quieras saber su precio: ")

print(diccionario.get(usuario.lower(), "No existe"), "€")