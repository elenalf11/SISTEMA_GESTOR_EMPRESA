def esPalindromo(palabra):
    inversa = palabra[::-1]

    if(palabra.lower() == inversa.lower()):
        return True
    else:
        return False
    
palabra = input("Dime una palabra: ")
if(esPalindromo(palabra)):
    print(f"La palabra {palabra} es palíndroma")
else:
    print(f"La palabra {palabra} no es palíndroma")