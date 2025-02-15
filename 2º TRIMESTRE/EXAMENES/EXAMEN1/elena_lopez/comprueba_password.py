letras = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F","G", "H", "J", "K", "L", "Ñ", "Z", "X", "C", "V", "B", "N", "M"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
especial = ["!|@#$%&/()=?¿^*"]
def compruebaPass (cadena):
    correcta = False
    if(len(cadena) == 8):
        for i in cadena:
            for j in letras:
                if(i == j and i == j.lower()):
                    for x in numeros:
                        if (i == x):
                            for y in especial:
                                if(i == y):
                                    correcta = True
                                    print("La contraseña es segura")
                                else:
                                    print("La contraseña no es segura")
                                    return
                        else:
                            print("La contraseña no es segura")
                            return
                else:
                    print("La contraseña no es segura")
                    return
                        


cadena = input("Dime tu contraseña: ")
compruebaPass(cadena)