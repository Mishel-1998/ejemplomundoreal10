import json
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                self.productos = [Producto(p["_id"], p["_nombre"], p["_cantidad"], p["_precio"]) for p in data if isinstance(p, dict)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = []

    def guardar_en_archivo(self):
        with open(self.archivo, "w") as f:
            json.dump([{
                "_id": p.get_id(),
                "_nombre": p.get_nombre(),
                "_cantidad": p.get_cantidad(),
                "_precio": p.get_precio()
            } for p in self.productos], f, indent=4)

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            return False
        self.productos.append(producto)
        self.guardar_en_archivo()
        return True

    def modificar_producto(self, pid, nombre, cantidad, precio):
        for p in self.productos:
            if p.get_id() == pid:
                p.set_nombre(nombre)
                p.set_cantidad(cantidad)
                p.set_precio(precio)
                self.guardar_en_archivo()
                return True
        return False

    def eliminar_producto(self, pid):
        for i, p in enumerate(self.productos):
            if p.get_id() == pid:
                del self.productos[i]
                self.guardar_en_archivo()
                return True
        return False

    def listar_productos(self):
        return self.productos
