# Función para invertir un diccionario
def invertir_diccionario(diccionario):
    # Crear un nuevo diccionario vacío para almacenar el resultado invertido
    diccionario_invertido = {}

    # Recorrer cada par clave-valor en el diccionario original
    for clave, valor in diccionario.items():
        # Añadir el valor original como nueva clave y la clave original como nuevo valor
        diccionario_invertido[valor] = clave

    # Devolver el diccionario invertido
    return diccionario_invertido


diccionario = {
    "Madrid" : 28001,
    "París" : 70123,
    "Berlín" : 10,
    "Aranjuez" : 28300 
}

# Invertir el diccionario
codigos_postales_ciudades = invertir_diccionario(diccionario)

# Imprimir el diccionario invertido
print(codigos_postales_ciudades)

