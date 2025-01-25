diccionario = {
    "Elena": 19,
    "Antonio": 5,
    "Juan": 50,
    "Ana": 40
}
edades = list(diccionario.values())
suma = 0
for i in range (len(edades)):
    suma += edades[i]

print(f"La suma de las edades es: {suma}")
