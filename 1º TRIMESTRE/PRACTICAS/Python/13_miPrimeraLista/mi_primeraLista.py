lista = [] 

while True:
    entrada = input("Introduce un número o palabra (escribe 'fin' para terminar): ")
   
    if entrada.lower() == "fin":  
        break
   
    lista.append(entrada)  

print("Los elementos en la lista son:", lista)
print("El primer elemento es ", lista[0])
print("El último elemento es ", lista[-1])