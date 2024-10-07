lista = [1, 5, 3, 7, 7, 4, 1]
print("La lista original es: ", lista)
num_reemplazar = int(input("Dime el número que quieras cambiar: "))
num_nuevo = int(input("Dime por qué número quieres cambiarlo: "))

for i in range (len(lista)):
    if(num_reemplazar == lista[i]):
        lista[i] = num_nuevo

print("La lista modificada es: ", lista)