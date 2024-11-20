inicio_rango = int(input("Dime desde donde quieres que empiece a generar: "))
final_rango = int(input("Dime hasta donde quieres que genere números: "))
cantidad = int(input("Dime cuantos numeros quieres que genere: "))
contador = 0
random = []

for i in range(inicio_rango, final_rango):
    random.append(i)

while(contador < cantidad):
    if(cantidad % 2 == 0):
        print(random[contador - 3])
    else:
        print(random[contador - 1])
    contador+=1