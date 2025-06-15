# promedio_clima_poo.py

class Temperatura:
    def __init__(self, temperaturas):
        # Encapsulamos la lista de temperaturas
        self.__temperaturas = temperaturas

    def get_temperaturas(self):
        return self.__temperaturas

class CalculoTemperatura(Temperatura):
    def __init__(self, temperaturas):
        # Usamos herencia para inicializar desde la clase base
        super().__init__(temperaturas)

    def calcular_promedio(self):
        temperaturas = self.get_temperaturas()
        return sum(temperaturas) / len(temperaturas)

def main():
    print("=== Programa en POO: Promedio Semanal del Clima ===")
    temperaturas = []
    for i in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {i}: "))
        temperaturas.append(temp)

    calculadora = CalculoTemperatura(temperaturas)
    promedio = calculadora.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
