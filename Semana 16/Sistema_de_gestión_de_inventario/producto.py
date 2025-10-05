class Producto:
    def __init__(self, pid, nombre, cantidad, precio):
        self._id = pid
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id
    def get_nombre(self):
        return self._nombre
    def get_cantidad(self):
        return self._cantidad
    def get_precio(self):
        return self._precio

    def set_nombre(self, nombre):
        self._nombre = nombre
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
    def set_precio(self, precio):
        self._precio = precio
