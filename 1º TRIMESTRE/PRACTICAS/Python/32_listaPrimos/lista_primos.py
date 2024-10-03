numero = int(input("Ingresa un número: "))

primos = []

for i in range(2, numero + 1):
    es_primo = True
    for j in range(2, i): 
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(i)

print("La lista de números primos es: ", primos)

