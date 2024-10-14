lista = [0, 1, 0, 3, 12, 0, 5]

for i in lista:
    if(i == 0):
        aux = i
        lista.remove(i)
        lista.append(aux)
print(f"La lista modificada es {lista}")