numero = int(input("Dime un número: "))
a = 0
b = 1

for i in range(numero):
    print(a, end=" ")
    a,b = b, a + b