import tkinter as tk
from tkinter import ttk, messagebox
from inventario import Inventario
from producto import Producto


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario")
        self.root.geometry("850x600")
        self.root.config(bg="#f5f6fa")

        # Estilo general
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#273c75", foreground="white")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="white", fieldbackground="white")

        # Encabezado
        encabezado = tk.Frame(self.root, bg="#273c75", height=80)
        encabezado.pack(fill="x")
        tk.Label(encabezado, text="Sistema de Gestión de Inventario", bg="#273c75",
                 fg="white", font=("Segoe UI", 18, "bold")).pack(pady=10)
        tk.Label(encabezado, text="Nombre: Cinthia Carrión  |  Carrera: Ingeniería en TI  |  Paralelo: A",
                 bg="#273c75", fg="white", font=("Segoe UI", 10)).pack()

        # Marco principal
        contenedor = tk.Frame(self.root, bg="#f5f6fa")
        contenedor.pack(pady=20, padx=20, fill="both", expand=True)

        # Campos de entrada
        form = tk.LabelFrame(contenedor, text="Datos del producto", bg="#f5f6fa", font=("Segoe UI", 11, "bold"))
        form.pack(fill="x", pady=10)

        labels = ["ID", "Nombre", "Cantidad", "Precio"]
        self.entries = {}
        for i, texto in enumerate(labels):
            tk.Label(form, text=texto + ":", bg="#f5f6fa", font=("Segoe UI", 10)).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(form, font=("Segoe UI", 10), width=25)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[texto.lower()] = entry

        # Botones CRUD
        botones = tk.Frame(form, bg="#f5f6fa")
        botones.grid(row=0, column=2, rowspan=4, padx=20)

        tk.Button(botones, text="Agregar", bg="#44bd32", fg="white", width=12, font=("Segoe UI", 10, "bold"),
                  command=self.agregar_producto).pack(pady=5)
        tk.Button(botones, text="Modificar", bg="#e1b12c", fg="white", width=12, font=("Segoe UI", 10, "bold"),
                  command=self.modificar_producto).pack(pady=5)
        tk.Button(botones, text="Eliminar", bg="#e84118", fg="white", width=12, font=("Segoe UI", 10, "bold"),
                  command=self.eliminar_producto).pack(pady=5)
        tk.Button(botones, text="Guardar", bg="#0097e6", fg="white", width=12, font=("Segoe UI", 10, "bold"),
                  command=self.guardar_datos).pack(pady=5)

        # Búsqueda
        busqueda_frame = tk.Frame(contenedor, bg="#f5f6fa")
        busqueda_frame.pack(fill="x", pady=10)
        tk.Label(busqueda_frame, text="Buscar:", bg="#f5f6fa", font=("Segoe UI", 10)).pack(side="left", padx=5)
        self.buscar_var = tk.StringVar()
        buscar_entry = tk.Entry(busqueda_frame, textvariable=self.buscar_var, width=30, font=("Segoe UI", 10))
        buscar_entry.pack(side="left", padx=5)
        buscar_entry.bind("<KeyRelease>", lambda e: self.actualizar_tabla())

        # Tabla
        tabla_frame = tk.Frame(contenedor)
        tabla_frame.pack(fill="both", expand=True)

        columnas = ("ID", "Nombre", "Cantidad", "Precio")
        self.tree = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
        self.tree.pack(fill="both", expand=True)

        # Barra de desplazamiento
        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Contador
        self.contador_label = tk.Label(contenedor, text="Total de productos: 0", bg="#f5f6fa", font=("Segoe UI", 10, "bold"))
        self.contador_label.pack(pady=5)

        # Atajos
        self.root.bind("<Delete>", lambda e: self.eliminar_producto())
        self.root.bind("<Escape>", lambda e: self.root.quit())

        # Inventario
        self.inventario = Inventario()
        self.inventario.cargar_desde_archivo()
        self.actualizar_tabla()

    # ---------------- FUNCIONES CRUD ----------------
    def agregar_producto(self):
        try:
            id_p = self.entries["id"].get()
            nombre = self.entries["nombre"].get()
            cantidad = int(self.entries["cantidad"].get())
            precio = float(self.entries["precio"].get())

            if not id_p or not nombre:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
                return

            if id_p in [p.id for p in self.inventario.listar_productos()]:
                messagebox.showerror("Error", f"Ya existe un producto con ID {id_p}.")
                return

            p = Producto(id_p, nombre, cantidad, precio)
            self.inventario.agregar_producto(p)
            self.inventario.guardar_en_archivo()
            self.actualizar_tabla()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Verifica que cantidad y precio sean numéricos.")

    def eliminar_producto(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            id_prod = self.tree.item(seleccionado)["values"][0]
            nombre = self.tree.item(seleccionado)["values"][1]

            confirmar = messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Estás seguro de eliminar el producto:\n\nID: {id_prod}\nNombre: {nombre} ?"
            )

            if confirmar:
                self.inventario.eliminar_producto(id_prod)
                self.inventario.guardar_en_archivo()
                self.actualizar_tabla()
                messagebox.showinfo("Éxito", f"✅ Producto '{nombre}' eliminado correctamente.")
        else:
            messagebox.showwarning("Atención", "Por favor selecciona un producto para eliminar.")

    def modificar_producto(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Info", "Selecciona un producto para modificar.")
            return

        try:
            id_p = self.tree.item(seleccionado)["values"][0]
            nombre = self.entries["nombre"].get()
            cantidad = int(self.entries["cantidad"].get())
            precio = float(self.entries["precio"].get())
            self.inventario.modificar_producto(id_p, nombre, cantidad, precio)
            self.inventario.guardar_en_archivo()
            self.actualizar_tabla()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Cantidad y precio deben ser numéricos.")

    def guardar_datos(self):
        self.inventario.guardar_en_archivo()
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        filtro = self.buscar_var.get().lower()
        productos = [p for p in self.inventario.listar_productos() if filtro in p.nombre.lower()]

        for p in productos:
            self.tree.insert("", tk.END, values=(p.id, p.nombre, p.cantidad, f"${p.precio:.2f}"))

        self.contador_label.config(text=f"Total de productos: {len(productos)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
