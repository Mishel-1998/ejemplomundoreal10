# Clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Subclase Perro que hereda de Animal
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

# Uso
mi_perro = Perro("Firulais")
mi_perro.comer()    # Método heredado
mi_perro.ladrar()   # Método propio de Perro

