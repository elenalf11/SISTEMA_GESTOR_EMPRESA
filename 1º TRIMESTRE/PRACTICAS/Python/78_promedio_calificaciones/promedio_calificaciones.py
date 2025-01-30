diccionario = {
    "Elena" : [10, 7, 6],
    "Pepe" : [5, 6, 3],
    "Manuel" : [1, 8, 4],
}

diccionario_nuevo = {}

for nombre, notas in diccionario.items():
    suma = sum(notas)
    media = suma / len(notas)
    diccionario_nuevo[nombre] = media


print(diccionario_nuevo)