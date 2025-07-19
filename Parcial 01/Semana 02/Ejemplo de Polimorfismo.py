# Clase base Instrumento
class Instrumento:
    def tocar(self):
        print("Este instrumento hace un sonido.")  # Comportamiento genérico

# Subclase Guitarra que redefine tocar
class Guitarra(Instrumento):
    def tocar(self):
        print("La guitarra suena: ¡Strum!")  # Comportamiento específico

# Subclase Piano que redefine tocar
class Piano(Instrumento):
    def tocar(self):
        print("El piano suena: ¡Plink plonk!")  # Comportamiento específico

# Uso del polimorfismo
instrumentos = [Guitarra(), Piano()]
for instrumento in instrumentos:
    instrumento.tocar()  # Cada instrumento usa su propia implementación
