letra = input("Dime una letra: ")

match letra.lower():
    case "a":
        print("Es vocal")
    case "e":
        print("Es vocal")
    case "i":
        print("Es vocal")
    case "o":
        print("Es vocal")
    case "u":
        print("Es vocal")
    case _:
        print("Es consonante o un carácter no válido")