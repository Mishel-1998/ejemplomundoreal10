from abc import ABC, abstractmethod

# ---------------------------
# S - Single Responsibility Principle
# Cada clase se enfoca en un solo tipo de procesamiento de pago.
# ---------------------------

# Clase abstracta que define la interfaz para procesadores de pago
class ProcesadorPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad: float):
        pass

# Clase concreta para pagos con tarjeta de crédito
class PagoTarjetaCredito(ProcesadorPago):
    def procesar_pago(self, cantidad: float):
        print(f"Procesando pago de ${cantidad:.2f} con Tarjeta de Crédito.")

# Clase concreta para pagos con PayPal
class PagoPayPal(ProcesadorPago):
    def procesar_pago(self, cantidad: float):
        print(f"Procesando pago de ${cantidad:.2f} con PayPal.")

# Clase concreta para pagos con Criptomonedas
class PagoCriptomoneda(ProcesadorPago):
    def procesar_pago(self, cantidad: float):
        print(f"Procesando pago de ${cantidad:.2f} con Criptomonedas.")

# ---------------------------
# D - Dependency Inversion Principle
# El servicio depende de una abstracción, no de implementaciones específicas.
# ---------------------------

class ServicioPago:
    def __init__(self, procesador: ProcesadorPago):
        self.procesador = procesador  # Inyección de dependencia

    def realizar_pago(self, cantidad: float):
        self.procesador.procesar_pago(cantidad)

# ---------------------------
# O - Open/Closed Principle
# Se puede extender con nuevos tipos de pago sin modificar código existente.
# ---------------------------

# Uso del sistema
tarjeta = ServicioPago(PagoTarjetaCredito())
paypal = ServicioPago(PagoPayPal())
cripto = ServicioPago(PagoCriptomoneda())

# ---------------------------
# Polimorfismo
# Cada clase concreta implementa el metodo procesar_pago con su propia lógica.
# ---------------------------

tarjeta.realizar_pago(100.0)
paypal.realizar_pago(59.99)
cripto.realizar_pago(250.75)
