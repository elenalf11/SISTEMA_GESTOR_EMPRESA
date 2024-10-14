operacion = input("Dime el símbolo de la operación que quieras hacer [+, -, *, /]: ")
num_1 = int(input("Dime un número: "))
num_2 = int(input("Dime otro número: "))

match operacion:
    case "+":
        suma = num_1 + num_2
        print(f"La suma entre {num_1} + {num_2} = {suma}")
    case "-":
        resta = num_1 - num_2
        print(f"La resta entre los números {num_1} - {num_2} = {resta}")
    case "*":
        multiplicacion = num_1 * num_2
        print(f"La multiplicación entre {num_1} * {num_2} = {multiplicacion}")
    case "/":
        division = num_1 / num_2
        print(f"La división entre {num_1} / {num_2} = {division}")
    case _:
        print("Operación no válida")