# Libros de Desarrollo Personal
# ----------------------------------------------------------
# El programa simula un sistema que gestiona libros de desarrollo personal:
#   - Clase base: Libro
#   - Clases derivadas: Ikigai y Gung Ho
#   - Atributo encapsulado: precio (con getter y setter)
#   - Metodo polimórfico: resumen(), que cambia según el libro

# Clase base
class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio  # Encapsulación

    # Getter del precio (encapsulación)
    def get_precio(self):
        return self.__precio

    # Setter del precio (encapsulación con validación)
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Precio inválido.")

    # Metodo que será sobrescrito (polimorfismo)
    def resumen(self):
        print("Resumen general del libro.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.__precio:.2f}")


# Clase derivada: Ikigai
# Hereda atributos y métodos de la clase Libro
class Ikigai(Libro):
    def __init__(self, precio):
        super().__init__("Ikigai", "Héctor García y Francesc Miralles", precio)

    def resumen(self):
        print("Este libro explora el concepto japonés de 'ikigai' o propósito de vida, "
              "y cómo encontrar la felicidad a través del equilibrio entre lo que amas, lo que eres bueno, "
              "lo que necesita el mundo y por lo que te pueden pagar.")


# Clase derivada: GungHo (¡A la carga!)
class GungHo(Libro):
    def __init__(self, precio):
        super().__init__("¡A la carga! (Gung Ho)", "Ken Blanchard y Sheldon Bowles", precio)

    def resumen(self):
        print("Gung Ho presenta una filosofía de liderazgo basada en tres principios inspirados en animales, "
              "con el objetivo de motivar a los equipos de trabajo: el espíritu de la ardilla, la manera del castor "
              "y el don del ganso.")


# Código principal
if __name__ == "__main__":
    # Crear instancias de los libros
    libro1 = Ikigai(15.99)
    libro2 = GungHo(12.50)

    # Mostrar información y aplicar polimorfismo
    print("\n--- Información del libro Ikigai ---")
    libro1.mostrar_info()
    libro1.resumen()

    print("\n--- Información del libro Gung Ho ---")
    libro2.mostrar_info()
    libro2.resumen()

    # Encapsulación: cambiar precio
    print("\n--- Cambiar precio del libro Ikigai ---")
    print("Precio actual:", libro1.get_precio())
    libro1.set_precio(-5)  # Intento inválido
    libro1.set_precio(17.00)
    print("Nuevo precio:", libro1.get_precio())
