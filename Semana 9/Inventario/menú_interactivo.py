from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()
    while True:
        print("\n== SISTEMA DE GESTIÓN DE INVENTARIO ==")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")

            try:
                cantidad = int(input("Cantidad (solo número): "))
            except ValueError:
                print("Error: la cantidad debe ser un número entero.")
                continue

            try:
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: el precio debe ser un número decimal.")
                continue

            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo_producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")

            cantidad_str = input("Nueva cantidad (dejar vacío si no cambia): ")
            cantidad = int(cantidad_str) if cantidad_str else None

            precio_str = input("Nuevo precio (dejar vacío si no cambia): ")
            precio = float(precio_str) if precio_str else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
