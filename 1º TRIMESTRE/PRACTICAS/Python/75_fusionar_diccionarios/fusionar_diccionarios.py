#Calificaciones Matematicas
diccionario_1 = {
    "Elena" : 10,
    "Juan" : 5,
    "María" : 4,
    "Paula" : 7,
    "Manuel" : 6
}

#Calificaciones Ciencias
diccionario_2 = {
    "Elena" : 7,
    "Juan" : 3,
    "María" : 5,
    "Paula" : 7,
    "Manuel" : 10,

}

diccionario_3 = diccionario_1.copy()

print(diccionario_3)


for i, j in diccionario_2.items():
    for j in diccionario_2.keys():
        diccionario_3[j] = diccionario_2[j] 

print(diccionario_3)