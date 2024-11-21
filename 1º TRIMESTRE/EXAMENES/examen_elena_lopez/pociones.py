def crearPocionMagica(pociones, meta):
    objetivo = meta
    num1 = 0
    num2 = 0
    for i in range (0, len(pociones)):
        for j in range(1, len(pociones) -1):
            num1 = pociones[i]
            num2 = pociones[j]
            if((num1 + num2) == objetivo):
                indice1 = i
                indice2 = j
                return [indice1, indice2] 
            
    return "undefined"



pociones = [4, 5, 6, 2]
meta = 5

print(crearPocionMagica(pociones, meta))