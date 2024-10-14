lados = int(input("Dime el número de lados de la figura que quieres: "))

match lados:
    case 1:
        print("Es una recta")
    case 2:
        print("Es un dígono")
    case 3:
        print("Es un triángulo")
    case 4:
        print("Es un cuadrilátero")
    case 5:
        print("Es un pentágono")
    case 6:
        print("Es un hexágono")
    case 7:
        print("Es un heptágono")
    case 8:
        print("Es un octógono")
    case 9:
        print("Es un eneágono o nonágono")
    case 10:
        print("Es un decágono")
    case _:
        print("El sistema no tiene más figuras")
