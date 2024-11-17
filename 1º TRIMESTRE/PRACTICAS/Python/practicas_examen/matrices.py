import random


numeros = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]

def crearMatriz_1(filas, columnas):
    matriz1 = [["X" for _ in range (filas)] for _ in range (columnas)]
    return matriz1

def printMatriz_1(matriz):
    for fila in matriz:
        print(" ".join(fila))

def crearMatriz_2(filas, columnas):
    matriz = []
    parejas = (filas * columnas)//2

    for i in range (0, parejas):
        matriz.extend([numeros[i], numeros[i]])

        matriz_descolocada = random.sample(matriz, len(matriz))

        matriz2 = [matriz_descolocada[j:(j + columnas)] for j in range(0, len(matriz_descolocada), columnas)]
    return matriz2

def printMatriz_2(matriz):
    for fila in matriz:
        print(" ".join(fila))
    

filas = int(input("Dime filas: "))
columnas = int(input("Dime columnas: "))

printMatriz_1(crearMatriz_1(filas, columnas))
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
printMatriz_2(crearMatriz_2(filas, columnas))

    