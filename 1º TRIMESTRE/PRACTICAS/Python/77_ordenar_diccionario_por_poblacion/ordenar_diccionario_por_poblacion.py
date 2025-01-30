diccionario = {
    "España" : 700,
    "Francia" : 680,
    "EEUU" : 33400,
    "Luxemburgo" : 66,
}

# Crea un diccionario donde la clave es el numero y el valor el pais
diccionario_invertido = {numero : pais for pais, numero in diccionario.items()}

paises_ordenado = sorted(diccionario_invertido.keys(), reverse = True)

# Reconstruimos el diccionario
diccionario_ordenado = {diccionario_invertido[pais] : pais for pais in paises_ordenado}

print(diccionario_ordenado)