opcion = input("¿Quieres convertir Fahrenheit(F) o Celsius(C)?")
if(opcion == "F"):
    temperaturaf = float(input("Dime la temperatura en Fahrenheit: "))
    conversorf = (temperaturaf - 32) * 5/9
    print(temperaturaf, " Fº equivale a ", conversorf, " Cº")
elif(opcion == "C"):
    temperaturac = float(input("Dime la temperatura en Celsius: "))
    conversorc = (temperaturac * 9/5) + 32
    print(temperaturac, "Cº equivale a ", conversorc, " Cº")


