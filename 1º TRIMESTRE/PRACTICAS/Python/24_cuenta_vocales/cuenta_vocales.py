palabra = input("Dime una palabra: ")
vocales = ['a', 'e', 'i', 'o']
contador = 0

for i in vocales:
    contador += palabra.lower().count(i)
    
print(contador)
    