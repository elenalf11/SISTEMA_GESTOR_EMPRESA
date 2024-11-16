def cuentaVocales(frase):
    vocales = 'aeiouáéíóú'
    cont = sum(1 for letra in frase.lower() if letra in vocales)
    return cont

frase = input("Dime una frase: ")
print(f"En la frase: {frase} hay {cuentaVocales(frase)} vocales")
