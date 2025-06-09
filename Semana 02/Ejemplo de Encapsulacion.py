## Definición de la clase InventarioProducto
class InventarioProducto:
    def __init__(self, nombre, stock):
        self.__nombre = nombre       # Atributo privado
        self.__stock = stock         # Atributo privado

    # Metodo para agregar productos al stock
    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad

    # Método para vender productos (restar del stock)
    def vender_producto(self, cantidad):
        if 0 < cantidad <= self.__stock:
            self.__stock -= cantidad
        else:
            print("Stock insuficiente")

    # Método para ver el stock actual
    def obtener_stock(self):
        return self.__stock

    # Método para obtener el nombre del producto
    def obtener_nombre(self):
        return self.__nombre

# Uso
producto = InventarioProducto("Lápiz", 100)
producto.agregar_stock(50)        # Agrega 50 unidades
producto.vender_producto(30)      # Vende 30 unidades
print("Producto:", producto.obtener_nombre())
print("Stock actual:", producto.obtener_stock())
