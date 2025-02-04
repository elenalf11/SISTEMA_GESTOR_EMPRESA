diccionario_1 = {
    "Antonio" : 50,
    "Andrea" : 37,
    "Carmen" : 25,
    "Elena" : 20
}

diccionario_2 = {}

for i, j in diccionario_1.items():
    if(j > 30):
        diccionario_2[i] = j
    else:
        pass

print(f"Diccionario 1: {diccionario_1}")
print(f"Diccionario 2: {diccionario_2}")