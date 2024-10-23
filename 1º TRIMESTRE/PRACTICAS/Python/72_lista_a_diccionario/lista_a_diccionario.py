lista = ["hola", "perro", "gato", "adios"]

for i in lista:
    dic = {list(lista).index(i) : i}
    print(dic)
