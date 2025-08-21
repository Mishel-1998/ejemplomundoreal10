import os  # Para verificar si el archivo existe
from producto import Producto  # Importamos la clase Producto

class GestionInventario:
    def __init__(self, nombre_archivo="inventario.txt"):
        """
        Inicializa la clase con el nombre del archivo donde se guardará el inventario.
        Por defecto se usará 'inventario.txt'.
        """
        self.nombre_archivo = nombre_archivo

    def guardar_productos(self, productos):
        """
        Guarda el inventario en el archivo como un 'diccionario' (clave = ID, valor = Producto).
        Cada línea representa un producto, con el formato usado en el método __str__().
        """
        try:
            with open(self.nombre_archivo, "w", encoding="utf-8") as f:
                # Encabezado del archivo
                f.write(f"{'ID':<5} | {'Nombre':<15} | {'Cantidad':<8} | {'Precio':<10}\n")
                f.write("-" * 50 + "\n")

                # Guardamos cada producto del diccionario
                for id_producto, producto in productos.items():
                    f.write(str(producto) + "\n")

            print(f"Inventario guardado en {self.nombre_archivo}")

        except PermissionError:
            print("Error: No se puede escribir en el archivo (archivo abierto o sin permisos).")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def cargar_productos(self, Producto):
        """
        Carga los productos desde el archivo y los almacena en un diccionario.
        Clave: ID del producto. Valor: Objeto Producto.
        Si el archivo no existe, lo crea vacío con encabezado.
        """
        productos = {}  # Diccionario vacío

        if not os.path.exists(self.nombre_archivo):
            # Si no existe, creamos el archivo con encabezado vacío
            with open(self.nombre_archivo, "w", encoding="utf-8") as f:
                f.write(f"{'ID':<5} | {'Nombre':<15} | {'Cantidad':<8} | {'Precio':<10}\n")
                f.write("-" * 50 + "\n")
            return productos

        # Si el archivo existe, lo abrimos y procesamos
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8") as f:
                lines = f.readlines()[2:]  # Saltamos las dos primeras líneas (encabezado)

                for line in lines:
                    parts = line.strip().split("|")
                    if len(parts) != 4:
                        continue  # Saltamos líneas mal formateadas

                    # Limpiamos y convertimos cada campo
                    id_producto = parts[0].strip()
                    nombre = parts[1].strip()
                    cantidad = int(parts[2].strip())
                    precio = float(parts[3].strip().replace("$", ""))

                    # Creamos el objeto Producto y lo agregamos al diccionario
                    productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)

        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f"Error al leer inventario: {e}")

        return productos