import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
from producto import Producto
from inventario import Inventario


# ----------- FUNCIONES DE INTERFAZ -----------
def mostrar_portada():
    portada = tk.Tk()
    portada.title("Universidad Estatal Amazónica - Portada")
    portada.geometry("1000x600")
    portada.resizable(False, False)
    portada.configure(bg="white")

    # Imagen de fondo
    try:
        ruta = os.path.join(os.path.dirname(__file__), "Portada. UEA.png")
        imagen = Image.open(ruta)
        imagen = imagen.resize((900, 400))
        fondo = ImageTk.PhotoImage(imagen)

        fondo_label = tk.Label(portada, image=fondo, bg="white")
        fondo_label.image = fondo
        fondo_label.pack(pady=(40, 10))
    except Exception as e:
        tk.Label(portada, text=f"Error cargando imagen: {e}", fg="red", bg="white").pack(pady=20)

    frame_botones = tk.Frame(portada, bg="white")
    frame_botones.pack(pady=10)

    def abrir_sistema():
        portada.destroy()
        mostrar_inventario()

    btn_ingresar = tk.Button(
        frame_botones, text="🗂  Ingresar al Sistema",
        bg="#004aad", fg="white", font=("Segoe UI", 13, "bold"),
        width=25, height=2, command=abrir_sistema,
        relief="flat", cursor="hand2", activebackground="#003580"
    )
    btn_ingresar.pack(side="left", padx=30)

    btn_salir = tk.Button(
        frame_botones, text="Salir",
        bg="#d32f2f", fg="white", font=("Segoe UI", 13, "bold"),
        width=25, height=2, command=portada.destroy,
        relief="flat", cursor="hand2", activebackground="#b71c1c"
    )
    btn_salir.pack(side="left", padx=30)

    tk.Label(
        portada, text="Presiona Escape para salir de la aplicación",
        font=("Segoe UI", 10), fg="green", bg="white"
    ).pack(side="bottom", pady=10)

    portada.bind("<Escape>", lambda e: portada.destroy())
    portada.mainloop()


# ----------- INTERFAZ DEL INVENTARIO -----------
def mostrar_inventario():
    inv = Inventario()
    inv.cargar_desde_archivo()

    ventana = tk.Tk()
    ventana.title("Sistema de Gestión de Inventario")
    ventana.geometry("1000x600")
    ventana.configure(bg="white")

    tk.Label(
        ventana, text="📦 Sistema de Gestión de Inventario",
        font=("Segoe UI", 18, "bold"), fg="#004aad", bg="white"
    ).pack(pady=20)

    # ------- CAMPOS -------
    frame_form = tk.Frame(ventana, bg="white")
    frame_form.pack(pady=10)

    tk.Label(frame_form, text="ID:", bg="white").grid(row=0, column=0, padx=5, pady=5)
    entry_id = tk.Entry(frame_form)
    entry_id.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Nombre:", bg="white").grid(row=1, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(frame_form)
    entry_nombre.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Cantidad:", bg="white").grid(row=2, column=0, padx=5, pady=5)
    entry_cantidad = tk.Entry(frame_form)
    entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Precio:", bg="white").grid(row=3, column=0, padx=5, pady=5)
    entry_precio = tk.Entry(frame_form)
    entry_precio.grid(row=3, column=1, padx=5, pady=5)

    # ------- TABLA -------
    columnas = ("ID", "Nombre", "Cantidad", "Precio")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=10)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
    tabla.pack(pady=20)

    def actualizar_tabla():
        tabla.delete(*tabla.get_children())
        for p in inv.listar_productos():
            tabla.insert("", "end", values=(p.id, p.nombre, p.cantidad, p.precio))

    # ------- FUNCIONES -------
    def agregar():
        try:
            id_p = entry_id.get()
            nombre = entry_nombre.get()
            cantidad = int(entry_cantidad.get())
            precio = float(entry_precio.get())

            if not id_p or not nombre:
                messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
                return

            producto = Producto(id_p, nombre, cantidad, precio)
            inv.agregar_producto(producto)
            actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "Cantidad o precio inválido.")

    def eliminar():
        seleccionado = tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Selecciona un producto", "Debes seleccionar un producto para eliminar.")
            return
        item = tabla.item(seleccionado)
        id_producto = item["values"][0]
        inv.eliminar_producto(id_producto)
        actualizar_tabla()
        messagebox.showinfo("Eliminado", "Producto eliminado correctamente.")

    def guardar():
        inv.guardar_en_archivo()
        messagebox.showinfo("Guardado", "Inventario guardado exitosamente.")

    # ------- BOTONES -------
    frame_botones = tk.Frame(ventana, bg="white")
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="Agregar", bg="#004aad", fg="white",
              font=("Segoe UI", 11, "bold"), width=12, command=agregar).grid(row=0, column=0, padx=10)
    tk.Button(frame_botones, text="Eliminar", bg="#d32f2f", fg="white",
              font=("Segoe UI", 11, "bold"), width=12, command=eliminar).grid(row=0, column=1, padx=10)
    tk.Button(frame_botones, text="Guardar", bg="#00796b", fg="white",
              font=("Segoe UI", 11, "bold"), width=12, command=guardar).grid(row=0, column=2, padx=10)
    tk.Button(frame_botones, text="Salir", bg="#9e9e9e", fg="white",
              font=("Segoe UI", 11, "bold"), width=12, command=ventana.destroy).grid(row=0, column=3, padx=10)

    actualizar_tabla()
    ventana.mainloop()


# -------- EJECUCIÓN --------
if __name__ == "__main__":
    mostrar_portada()
