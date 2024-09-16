anchura = int(input("Dime la anchura del rectángulo: "))
altura = int(input("Dime la altura del rectángulo: "))

#range (inicio, fin, incremento)
for i in range(altura):
    for j in range (anchura):
        print ("* ", end="")
    print()