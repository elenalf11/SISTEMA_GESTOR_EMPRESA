letras = {
    "a" : "4",
    "e" : "3",
    "i" :"1",
    "o" : "*",
    "u" : "_",
    "t" : "¡",
    "g" : "@",
    "p" : "?"
}

def encriptador(chain):
    new_chain = ""
    for i in letras.keys():
        for j in chain:
            if(j.lower() == i):
                j = letras[i]
                new_chain += j
            else:
                pass
        if(len(new_chain) == len(chain)):
            return new_chain

def desencriptador(chain):
    new_chain = ""
    for i in letras.values():
        for j in chain:
            if(j.lower() == i):
                j = letras[i]
                new_chain += j
            else:
                new_chain += j
        if(len(new_chain) == len(chain)):
            return new_chain

   

cadena = input("Dime una cadena de texto: ")
print(f"Cadena encriptada " + encriptador(cadena))
print(f"Cadena desencriptada " + desencriptador(cadena))