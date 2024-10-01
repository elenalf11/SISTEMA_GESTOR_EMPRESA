lista=[2,3,4,5,2,6,9,6]
print("Lista original: ", lista)

for i in range(len(lista)):
    for j in range(len(lista)-i-1):
        if lista[j]>lista[j+1]:
            aux = lista[j+1]
            lista[j+1] = lista[j]
            lista[j]=aux
        
        if lista[j]==lista[j+1] :
            lista.remove(lista[j])

print("Lista sin repetidos: ", lista)