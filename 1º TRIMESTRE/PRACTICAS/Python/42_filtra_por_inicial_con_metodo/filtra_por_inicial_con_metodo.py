palabras = ["sol", "luna", "mar", "estrella", "cielo", "sal"]

print("Esta es la lista: ", palabras)

letra = input("Dime la inicial de la palabra que quieras buscar: ")

busqueda = []

for i in palabras:

    if i.startswith(letra):

        busqueda.append(i)

#print("Las palabras que empiezan por la letra '", letra, "' son/es: ", busqueda)
print(f"Las palabras que empiezan por la letra {letra} son/es {busqueda}")