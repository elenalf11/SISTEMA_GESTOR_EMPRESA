lista = [1, "hola", 3.14, True, 42, "mundo", False]
enteros = []
texto = []
booleanos = []
otros = []

for i in lista:
    elemento = i
    match elemento:
        case str():
            texto.append(elemento)
        case True | False:
            booleanos.append(elemento)
        case int():
            enteros.append(elemento)
        case _:
            otros.append(elemento)


print(f"La lista de String es: {texto}")
print(f"La lista de booleanos es: {booleanos}")
print(f"La lista de Integer es: {enteros}")
print(f"La lista de Otros elementos es: {otros}")
