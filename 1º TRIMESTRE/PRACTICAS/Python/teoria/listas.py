# mi_lista = [1, 2, "hola", True]
# mi_lista.append(3) #Agregar un elemento al final
# #print(mi_lista)
# mi_lista.remove(2) #Eliminar un elemento
# #print(mi_lista)
# mi_lista.pop() #Eliminar el último elemento
# #print(mi_lista)
# #print("Mi lista tiene una longitud de ", len(mi_lista)) #Obtener la longitud de la lista
# mi_lista.extend([5, 6]) #Agregar una lista a otra 
# #print(mi_lista)
# mi_lista.insert(1, "pepe") #Insertar un elemento en una posición
# #print(mi_lista)
# #print("El elemento 2 aparece en la posición: ", mi_lista.index(1)) #Obtener la posición de un elemento
# #print("El elemento 5 aparecen en la lista ", mi_lista.count(5), "veces") #Obtener el número de veces que aparece un elemento
# lista_desordenada = [5, 3, 1, 9, 4]
# #print("La lista: ", lista_desordenada, " así esta ordenada de menos a mayor: ", sorted(lista_desordenada)) #Ordenar una lista de menor a mayor
# #print("La lista: ", lista_desordenada, " así esta ordenada de mayor a menor: ", sorted(lista_desordenada, reverse=True)) #Ordenar una lista de mayor a menor
# lista_desordenada.clear() #Limpiar una lista
# #print(lista_desordenada)
# nueva_lista = mi_lista.copy() #Copiar una lista
# #print(nueva_lista)
# lista = []  # Lista vacía para almacenar los datos

# #while True:
#     #entrada = input("Introduce un número o palabra (escribe 'fin' para terminar): ")
   
#     #if entrada.lower() == "fin":  # Si el usuario escribe 'fin', se termina el bucle
#         #break
   
#     #lista.append(entrada)  # Agrega la entrada a la lista

# #print("Los elementos en la lista son:", lista)
# #lista1 = [1, 0, 2, 6, 3, 2]
# #lista2 = [1:3] [0, 2] un rango específico
# #lista3 = [1:6:2] [0, 6, 2] un rango específico con saltos

# lista4 = ["Hola mundo", 3, 4, "pepe"]
# lista4[1:3] = ["Hola", "pepe2"]
# #print(lista4)
# #help(list) #Modo ayuda
# lista5 = [1, 2, 3, 4, 5]
# #print(3 in lista5)
# #print(6 in lista5)
# lista6 = [1, 2, 3]
# #print(lista6 < lista5)

# #x = [1, 2, 3['p', 'q'[5, 6, 7]]]
# #print(x[3][0])
# #print(x[3][2][0])
# #print(x[3][2][2])
# #y = [5, 9, 10]
# #for index, i in enumerate(y):
#     #print(index, i)
# #frutas = ["manzana", "banana", "cereza"]
# #for indice, fruta in enumerate (frutas):
#     #print(indice, fruta)

# lista7 = [5, 9, 10]
# lista8 = ["Jazz", "Rock", "Djent"]
# for i1, i2 in zip (lista7, lista8):
#     print(i1, i2)

mi_lista = [10, "Python", False, [4, 5, 6]]
print(mi_lista[0] + 5)
print(mi_lista[1].upper())
print(mi_lista[2] or True)
if "Python" in mi_lista:
    print("La palabra 'Python' está en la lista")
mi_lista[3][0] = 100
print(mi_lista[3][1])

dia = "hola"
match dia:
    case "Lunes":
        print("Es el inicio de la semana")
    case "Viernes":
        print("Ya casi es fin de semana")
    case "sábado | domingo":
        print("Es fin de semana")
    case _:
        print("El resto de día")

#Crear juego de las parejas
#Modos de juego:
#J1 vs J2 (ver partida)
#J1 vs CPU (ver partida)
#CPU vs CPU (ver partida o mostrar solo final)
#Iconos del tablero con emojis(preferiblemente)
#Tablero (preferiblemente) tamaño dinámico



nombre = "Elena"
edad = 19
print(f"Hola, {nombre}. Tienes {edad} años.")

t = 12345, 54321, "hello!"
print(t[0])
print(t)

tupla = (3, 4, 5)
size = len(tupla)
if(size == 1):
    print(f"La tupla es: {tupla}")
elif(size == 2):
    suma = tupla[0] + tupla[1]
    print(f"La suma de los dos números es: {tupla[0]} + {tupla[1]} = {suma}")
elif(size == 3):
    multiplicación = tupla[0] * tupla[1] * tupla[2]
    print(f"La multiplicación entre {tupla[0]} x {tupla[1]} x {tupla[2]} = {multiplicación}")
else:
    print("La tupla tiene más de 3 elementos o no continene solo números")

#Diccionario
id = {"elena":19, "pepe": 1}

diccionario_1 = {
    "Nombre": "Elena",
    "Edad": 25,
}

print(diccionario_1)

calificaciones = {"Ana":90, "Juan":85, "Pedro":78}
print(calificaciones["Ana"])

diccionario_2 = ([
    ("Nombre", "Elena"),
    ("Edad", 19),
])

print(diccionario_2)

diccionario_1["Nombre"] = "Pepe"
print(diccionario_1)

diccionario_1["Curso"] = "2ºDAM"
print(diccionario_1)

for i in diccionario_1:
    print(i)

for i in diccionario_1:
    print(i, diccionario_1[i])

for i, j in diccionario_1.items():
    print(i, j)

anidado1 = {"a": 1, "b": 2}
anidado1.clear()
print(anidado1)

d = {"a": 1, "b": 2}
print(d.get("a"))
print(d.get("z", "No encontrado"))

it = d.items()
print(it)

print(list(d))
print(list(d)[0][0])

k = d.keys()
print(k)
print(list(k))

v = d.values()
print(v)
print(list(v))

#d.pop("a")
d.pop("z", "No encontrado")
print(d)

d.popitem()
print(d)

d1 = {"a":1, "b":2}
d2 = {"a":0, "d":400}

d1.update(d2)
print(d1)

print(list(d))
print(sorted(d))