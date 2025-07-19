# promedio_clima_tradicional.py

def ingresar_temperaturas():
    """Solicita las temperaturas de los 7 días de la semana."""
    temperaturas = []
    for i in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {i}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula y retorna el promedio semanal de las temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    print("=== Programa Tradicional: Promedio Semanal del Clima ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()



