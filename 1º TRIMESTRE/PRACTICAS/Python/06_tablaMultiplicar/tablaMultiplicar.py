numeroInicio = float(input("Dime de qué número quieres saber la tabla de multiplicar: "))
numeroFinal = int(input("Dime hasta que número quieres que te haga la tabla de multiplicar: "))

for i in range(0, numeroFinal):
    print(numeroInicio, " x ", i, " = ", numeroInicio*i)
print()