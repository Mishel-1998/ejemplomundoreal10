import json
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]

    def modificar_producto(self, id_producto, nombre, cantidad, precio):
        if id_producto in self.productos:
            self.productos[id_producto].set_nombre(nombre)
            self.productos[id_producto].set_cantidad(cantidad)
            self.productos[id_producto].set_precio(precio)

    def listar_productos(self):
        return list(self.productos.values())

    def guardar_en_archivo(self, archivo="inventario.json"):
        data = {id: vars(p) for id, p in self.productos.items()}
        with open(archivo, "w") as f:
            json.dump(data, f, indent=4)

    def cargar_desde_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                for id, datos in data.items():
                    # Convertimos la clave 'id' del JSON en 'id_producto'
                    self.productos[id] = Producto(
                        id_producto=datos["id"],
                        nombre=datos["nombre"],
                        cantidad=datos["cantidad"],
                        precio=datos["precio"]
                    )
        except FileNotFoundError:
            pass

