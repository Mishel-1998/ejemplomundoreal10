from producto import Producto
from archivo import GestionInventario

class Inventario:
    def __init__(self):
        """
        Inicializa un inventario como diccionario.
        Carga automáticamente los productos existentes desde el archivo TXT.
        """
        self.gestor = GestionInventario()
        self.productos = self.gestor.cargar_productos(Producto)  # Diccionario: ID -> Producto

    def agregar_producto(self, producto):
        """
        Agrega un producto si su ID no existe aún.
        """
        if producto.get_id() in self.productos:
            print("El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado.")
            self.gestor.guardar_productos(self.productos)

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID, si existe.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
            self.gestor.guardar_productos(self.productos)
        else:
            print("No se encontró el producto.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza cantidad y/o precio de un producto si el ID existe.
        """
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    return
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo.")
                    return
                producto.set_precio(nuevo_precio)
            print("Producto actualizado.")
            print(producto)
            self.gestor.guardar_productos(self.productos)
        else:
            print("No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        """
        Devuelve una lista de productos que contienen el texto en su nombre (sin importar mayúsculas).
        """
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        """
        Muestra todos los productos en formato tabular simple (sin PrettyTable).
        """
        if not self.productos:
            print("Inventario vacío.")
            return

        # Encabezados
        print(f"{'ID':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10}")
        print("-" * 55)

        # Filas
        for p in self.productos.values():
            print(f"{p.get_id():<10} {p.get_nombre():<20} {p.get_cantidad():<10} ${p.get_precio():<10.2f}")
