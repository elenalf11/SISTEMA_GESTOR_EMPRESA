dia = input("Dime un día de la semana: ")

match dia.lower():
    case "lunes":
        print("El lunes es laborable")
    case "martes":
        print("El martes es laborable")
    case "miércoles":
        print("El miércoles es laborable")
    case "jueves":
        print("El jueves es laborable")
    case "viernes":
        print("El viernes es laborable")
    case "sábado":
        print("El sábado no es laborable, es fin de semana")
    case "domingo":
        print("El domingo no es laborale, es fin de semana")
    case _:
        print("Ese día no existe o no lo has escrito bien")