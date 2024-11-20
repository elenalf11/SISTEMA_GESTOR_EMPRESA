def esCapicua(numero):
    numero_invertido = numero[::-1]
    if(numero == numero_invertido):
        return True
    else:
        return False
    
def calculadora(num1, num2, operacion):
    match operacion.lower():
        case "suma":
            suma = num1 +num2
            print(f"La suma entre {num1} + {num2} es = {suma}")
        case "resta":
            if(num1 > num2):
                resta = num1 - num2
                print(f"La resta entre {num1} - {num2} es = {resta}")
            else:
                resta = num2 - num1
                print(f"La resta entre {num2} - {num1} es = {resta}")
        case "multiplicación":
            multiplicacion = num1 * num2
            print(f"La multiplicación entre {num1} * {num2} es = {multiplicacion}")
        case "potencia":
            potencia = num1 ** num2
            print(f"{num1} elevado a {num2} es = {potencia}")
        case "división":
            division = num1 // num2
            print(f"La división entre {num1} / {num2} es = {division}")
        case "resto":
            resto = num1 % num2
            print(f"El resto entre {num1} y {num2} es = {resto}")

num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))
operación = input("Dime que operación quieres realizar (suma-resta-multiplicación-potencia-división-resto): ")
calculadora(num1, num2, operación)

