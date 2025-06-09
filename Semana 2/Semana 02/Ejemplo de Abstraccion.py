from abc import ABC, abstractmethod
import math

# Clase abstracta Figura
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Subclase Circulo que implementa calcular_area
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Subclase Cuadrado que implementa calcular_area
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

# Uso
figuras = [Circulo(3), Cuadrado(4)]

for figura in figuras:
    print(f"Área: {figura.calcular_area():.2f}")
