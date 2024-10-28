#Creando una clase vacía
class Perro:
    especie = "mamífero"
    #Constructora 
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")
    
    def ladra(self):
        print("Guau")
    
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

    @classmethod
    def metododeclase (cls):
        return "Método de clase", cls


mi_perro = Perro("Toby", "Bulldog")
print(type(mi_perro))
mi_perro.ladra()
mi_perro.camina(10)