temperatura = int(input("Dime la temperatura que hace: "))

match temperatura:
    case temperatura if(temperatura < 0):
        print("Hoy hace mucho frío")
    case temperatura if(0 <= temperatura <= 10):
        print("Hoy hace frío")
    case temperatura if(11 <= temperatura <= 20):
        print("Hoy estará templado")
    case temperatura if(21 <= temperatura <= 30):
        print("Hoy hace calor")
    case temperatura if(temperatura > 30):
        print("Hoy hace mucho calor")