# sistema_seguros.py

# Clase que representa una póliza de seguros
# Sistema de seguros para la empresa Conseseg Cia. Tdla
class Poliza:
    def __init__(self, codigo, tipo, valor_anual):
        # Atributos de la póliza
        self.codigo = codigo                 # Código identificador
        self.tipo = tipo                     # Tipo de seguro: Vida, Vehículo, Salud, etc.
        self.valor_anual = valor_anual       # Costo anual del seguro
        self.disponible = True               # Indica si la póliza está disponible

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Contratada"
        print(f"Póliza {self.codigo} - Tipo: {self.tipo} - Valor Anual: ${self.valor_anual} - Estado: {estado}")

    def contratar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def liberar(self):
        self.disponible = True


# Clase que representa al cliente que contrata un seguro
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        print(f"Cliente: {self.nombre} - Cédula: {self.cedula}")


# Clase que representa el contrato de una póliza con un cliente
class Contrato:
    def __init__(self, cliente, poliza, anios):
        self.cliente = cliente
        self.poliza = poliza
        self.anios = anios
        self.total = self.poliza.valor_anual * anios  # Se calcula el total

    def mostrar_detalle(self):
        print(f"\n--- Detalle del Contrato ---")
        self.cliente.mostrar_info()
        print(f"Póliza {self.poliza.codigo} - Tipo: {self.poliza.tipo}")
        print(f"Años: {self.anios} - Total a pagar: ${self.total}")


# Clase principal que gestiona las pólizas y contratos
class Aseguradora:
    def __init__(self, nombre):
        self.nombre = nombre
        self.polizas = []     # Lista de objetos Poliza
        self.contratos = []   # Lista de objetos Contrato

    def agregar_poliza(self, poliza):
        self.polizas.append(poliza)

    def mostrar_polizas(self):
        print(f"\n--- Pólizas disponibles en {self.nombre} ---")
        for pol in self.polizas:
            pol.mostrar_info()

    def contratar_poliza(self, cedula, nombre, tipo_poliza, anios):
        for pol in self.polizas:
            if pol.tipo == tipo_poliza and pol.disponible:
                cliente = Cliente(nombre, cedula)
                if pol.contratar():
                    contrato = Contrato(cliente, pol, anios)
                    self.contratos.append(contrato)
                    print("\n¡Contrato realizado con éxito!")
                    contrato.mostrar_detalle()
                    return
        print("\nNo hay pólizas disponibles del tipo solicitado.")

    def mostrar_contratos(self):
        print(f"\n--- Contratos registrados en {self.nombre} ---")
        if not self.contratos:
            print("No hay contratos registrados.")
        for contrato in self.contratos:
            contrato.mostrar_detalle()


# Bloque de prueba que demuestra la funcionalidad del sistema
if __name__ == "__main__":
    # Crear aseguradora
    conseseg = Aseguradora("Conseseg Cía. Ltda.")

    # Agregar pólizas al sistema
    conseseg.agregar_poliza(Poliza("VID001", "Vida", 450))
    conseseg.agregar_poliza(Poliza("AUT002", "Vehículo", 600))
    conseseg.agregar_poliza(Poliza("SAL003", "Salud", 700))
    conseseg.agregar_poliza(Poliza("HOG004", "Hogar", 550))
    conseseg.agregar_poliza(Poliza("VID005", "Vida", 500))

    # Mostrar las pólizas disponibles
    conseseg.mostrar_polizas()

    # Contratar pólizas
    conseseg.contratar_poliza("0923486723", "Cinthia Carrion", "Vida", 5)
    conseseg.contratar_poliza("1102953178", "Mishel Carrion", "Vehículo", 3)

    # Intentar contratar una póliza no disponible
    conseseg.contratar_poliza("0105362481", "Alexis Mafla", "Vehículo", 2)

    # Mostrar pólizas luego de contratar
    conseseg.mostrar_polizas()

    # Mostrar contratos realizados
    conseseg.mostrar_contratos()
