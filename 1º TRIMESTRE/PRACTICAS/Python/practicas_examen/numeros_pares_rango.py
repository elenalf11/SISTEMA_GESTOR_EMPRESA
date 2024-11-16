num1 = int(input("Dime un número: "))
num2 = int(input("Dime otro número: "))

pares = []

for i in range(num1,num2):
    if(i % 2 == 0):
        pares.append(i)

if(num2 % 2 == 0):
    pares.append(num2)
    
print(pares)