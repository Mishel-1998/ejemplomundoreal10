"""Sistema de Reservación de Vuelos usando constructores y destructores.
Este programa define tres clases principales: Vuelo, Pasajero y Reservacion.
Cada clase incluye un constructor (__init__) y un destructor (__del__),
para demostrar cómo se crean y destruyen los objetos en Python."""

class Vuelo:
    def __init__(self, numero, destino):
        """Constructor de la clase Vuelo. Inicializa el número de vuelo y el destino."""
        self.numero = numero
        self.destino = destino
        print(f"[VUELO CREADO] Vuelo {self.numero} hacia {self.destino} ha sido programado.")

    def mostrar_info(self):
        """Muestra la información del vuelo."""
        print(f"Vuelo N° {self.numero} con destino a {self.destino}")

    def __del__(self):
        """Destructor de la clase Vuelo."""
        print(f"[VUELO ELIMINADO] Vuelo {self.numero} ha sido cancelado o finalizado.")


class Pasajero:
    def __init__(self, nombre):
        """Constructor de la clase Pasajero."""
        self.nombre = nombre
        print(f"[PASAJERO REGISTRADO] {self.nombre} ha sido agregado al sistema.")

    def mostrar_info(self):
        """Muestra la información del pasajero."""
        print(f"Pasajero: {self.nombre}")

    def __del__(self):
        """Destructor de la clase Pasajero."""
        print(f"[PASAJERO ELIMINADO] {self.nombre} ha sido removido del sistema.")


class Reservacion:
    def __init__(self, pasajero, vuelo):
        """Constructor de la clase Reservacion."""
        self.pasajero = pasajero  # Composición
        self.vuelo = vuelo        # Composición
        print(f"[RESERVACIÓN REALIZADA] {pasajero.nombre} reservó el vuelo {vuelo.numero} a {vuelo.destino}.")

    def mostrar_info(self):
        """Muestra la información de la reservación."""
        print(f"{self.pasajero.nombre} tiene una reservación para el vuelo {self.vuelo.numero} con destino a {self.vuelo.destino}.")

    def __del__(self):
        """Destructor de la clase Reservacion."""
        print(f"[RESERVACIÓN CANCELADA] Vuelo {self.vuelo.numero} para {self.pasajero.nombre} ha sido cancelado.")


# FUNCIÓN PRINCIPAL
def main():
    vuelo1 = Vuelo("AF123", "París")
    pasajero1 = Pasajero("Laura Mendoza")
    reservacion1 = Reservacion(pasajero1, vuelo1)

    print("\n--- Información de la reservación ---")
    reservacion1.mostrar_info()

    # Al finalizar la función, se ejecutan los destructores automáticamente

# Ejecutar el programa
if __name__ == "__main__":
    main()
