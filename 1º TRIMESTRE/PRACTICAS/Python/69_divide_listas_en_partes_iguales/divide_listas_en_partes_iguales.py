def dividir_listas(lista, num):
    size = len(lista)
    division = size // num
    extra = size % num

    resultado = []
    j = 0

    for i in range(num):
        fin = j + division + (1 if extra < num else 0)
        resultado.append(lista[j : fin])
        j = fin
    
    return resultado

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num = int(input(f"Dime en cuántas partes quieres dividir la lista: "))
print(dividir_listas(lista, num))
