numero = int(input("Dime cuantos números quieres que muestre: "))

a, b = 0, 1

for i in range (numero):
   print(a, end=' ')
   a,b = b, a + b
