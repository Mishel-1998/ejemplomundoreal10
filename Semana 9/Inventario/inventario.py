class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """Añadir nuevo producto si el ID es único"""
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Producto ya existente")
        else:
            self.productos.append(producto)
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        """Eliminar producto por su ID."""
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualizar cantidad o precio de un producto"""
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado.")
                return
        print("No se encontró producto con ese ID.")

    def buscar_producto(self, nombre):
        """Buscar producto por nombre"""
        encontrados = [p for p in self.productos if p.get_nombre() == nombre]
        if encontrados:
            print("\nProductos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Mostrar productos del inventario"""
        if not self.productos:
            print("Inventario vacío.")
        else:
            print("\nLista de productos en inventario:")
            for p in self.productos:
                print(p)

