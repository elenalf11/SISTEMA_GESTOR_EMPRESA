lista = [1, 2, 3, 3]
contador = 0
for i in range(len(lista)):
    contador = 0
    for j in range(len(lista)):
        if(lista[i] == lista[j]):
            contador += 1
    print(lista[i], ":", contador)       
            
            
   
