diccionario_1 = {
    "Elena" : 8,
    "Pepe" : 7,
    "María" : 5,
    "Juan" : 3
}

diccionario_2 = {
    "Elena" : 10,
    "Pepe" : 5,
    "María" : 2,
    "Juan" : 6
}

diccionario_3 = {}

for key in diccionario_1.keys():
    if(diccionario_2[key] > diccionario_1[key]):
        diccionario_3[key] = diccionario_2[key]
    else:
        pass
print(f"Diccionario 1: {diccionario_1} \nDiccionario 2: {diccionario_2} \nDiccionario 3: {diccionario_3}")
            