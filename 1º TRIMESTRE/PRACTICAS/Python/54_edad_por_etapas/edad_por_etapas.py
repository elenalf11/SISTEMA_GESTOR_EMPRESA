edad = int(input("Dime tu edad y te diré en qué etapas estás: "))

match edad:
    case edad if(0 <= edad <= 12):
        print("Eres un niño")
    case edad if(13 <= edad <= 17):
        print("Eres adolescente")
    case edad if(18 <= edad <= 64):
        print("Eres adulto")
    case edad if(edad >= 65):
        print("Eres anciano")