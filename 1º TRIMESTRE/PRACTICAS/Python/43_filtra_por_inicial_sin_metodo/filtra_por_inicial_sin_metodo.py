palabras = ["sol", "luna", "mar", "estrella", "cielo"]

print("Esta es la lista: ", palabras)

letra = input("Dime la inicial de la palabra que quieras buscar: ")

busqueda = []

for i in palabras:

    if i[0] == letra.lower():

        busqueda.append(i)
        
print("Las palabras que empiezan por la letra '", letra, "' son/es: ", busqueda)