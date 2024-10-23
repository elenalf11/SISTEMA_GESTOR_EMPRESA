lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

num = int(input("Dime un número: "))

lista_final = []

print(f"La lista original es: {lista}")

for i in lista:
    #Si el elemento aparece n veces o menos, lo añadimos a la nueva lista lista_final
    if (lista.count(i) <= num):
        lista_final.append(i)
print(f"La lista final es: {lista_final}")