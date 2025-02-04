diccionario = {
    "Naranjas" : 15,
    "Manzanas" : 25,
    "Plátanos" : 50,
    "Calabaza" : 30
}

def agregar_productos (clave, valor):
    for key in diccionario.keys():
        if(clave == key):
            pass
        else:
            diccionario[clave] = valor
            print("Producto añadido al inventario")
            return
   

def quitar_productos (clave):
    for key in diccionario.keys():
        if(clave == key):
            diccionario.pop(clave)
            print("Producto eliminado del inventario")
            return
        else:
            pass

def modificar_stock (clave, stock):
    for key in diccionario.keys():
        if(clave == key):
            diccionario[clave] = stock
            print("Stock actualizado correctamente")
            return
        else:
            pass

def menu ():
    print("1. Añadir productos \n2. Eliminar productos \n3. Modificar stock \n4. Mostrar inventario")
    option = input("SELECT: ")
    match(option):
        case "1":
            clave = input("Dime que producto quieres añadir: ")
            valor = int(input("Dime el stock de tu producto: "))
            agregar_productos(clave, valor)
            print(diccionario)
        case "2":
            clave = input("Dime que producto quieres eliminar: ")
            quitar_productos(clave)
            print(diccionario)
        case "3":
            clave = input("Dime que producto quieres modificar: ")
            stock = int(input("Dime el nuevo stock de tu producto: "))
            modificar_stock(clave, stock)
            print(diccionario)
        case "4":
            print(diccionario)
        case _:
            print("Opción inválida")

menu()