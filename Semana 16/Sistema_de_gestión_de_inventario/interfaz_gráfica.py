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
        tk.Label(portada, text=f"⚠️ Error cargando imagen: {e}", fg="red", bg="white").pack(pady=20)

    # Botones debajo de la imagen
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
        frame_botones, text="❌ Salir",
        bg="#d32f2f", fg="white", font=("Segoe UI", 13, "bold"),
        width=25, height=2, command=portada.destroy,
        relief="flat", cursor="hand2", activebackground="#b71c1c"
    )
    btn_salir.pack(side="left", padx=30)

    portada.bind("<Escape>", lambda e: portada.destroy())
    portada.mainloop()


def mostrar_inventario():
    inv = Inventario()
    inv.cargar_desde_archivo()

    ventana = tk.Tk()
    ventana.title("📦 Sistema de Gestión de Inventario")
    ventana.geometry("1000x600")
    ventana.configure(bg="white")

    tk.Label(
        ventana, text="📦 Sistema de Gestión de Inventario",
        font=("Segoe UI", 18, "bold"), fg="#004aad", bg="white"
    ).pack(pady=20)

    # ------- FORMULARIO -------
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

    # ------- FUNCIONES -------
    def limpiar_campos():
        entry_id.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_precio.delete(0, tk.END)

    def actualizar_tabla():
        tabla.delete(*tabla.get_children())
        for p in inv.listar_productos():
            tabla.insert("", "end", values=(p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio()))

    def seleccionar_producto(event):
        try:
            item = tabla.selection()[0]
            valores = tabla.item(item, "values")
            entry_id.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            entry_id.insert(0, valores[0])
            entry_nombre.insert(0, valores[1])
            entry_cantidad.insert(0, valores[2])
            entry_precio.insert(0, valores[3])
        except IndexError:
            pass

    tabla.bind("<<TreeviewSelect>>", seleccionar_producto)

    def agregar():
        try:
            id_p = entry_id.get()
            nombre = entry_nombre.get()
            cantidad = int(entry_cantidad.get())
            precio = float(entry_precio.get())

            if not id_p or not nombre:
                messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")
                return

            if any(p.get_id() == id_p for p in inv.listar_productos()):
                messagebox.showerror("Duplicado", f"Ya existe un producto con ID {id_p}.")
                return

            producto = Producto(id_p, nombre, cantidad, precio)
            inv.agregar_producto(producto)
            actualizar_tabla()
            limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "La cantidad o el precio deben ser numéricos.")

    def modificar():
        seleccionado = tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un producto para modificar.")
            return
        try:
            id_p = entry_id.get()
            nombre = entry_nombre.get()
            cantidad = int(entry_cantidad.get())
            precio = float(entry_precio.get())
            exito = inv.modificar_producto(id_p, nombre, cantidad, precio)
            if exito:
                actualizar_tabla()
                limpiar_campos()
            else:
                messagebox.showerror("Error", f"No se pudo modificar. Verifica que el ID '{id_p}' exista.")
        except ValueError:
            messagebox.showerror("Error", "Verifica que los valores sean correctos.")

    def eliminar():
        seleccionado = tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar.")
            return
        item = tabla.item(seleccionado[0])
        id_producto = str(item["values"][0]).zfill(3)
        confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Eliminar el producto con ID {id_producto}?")
        if confirmar:
            exito = inv.eliminar_producto(id_producto)
            if exito:
                actualizar_tabla()
                limpiar_campos()
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el producto. Revisa que el ID '{id_producto}' exista.")

    def buscar_por_id():
        pid = entry_id.get().strip()
        if not pid:
            messagebox.showwarning("Advertencia", "Ingresa un ID para buscar.")
            return
        encontrado = None
        for p in inv.listar_productos():
            if p.get_id() == pid:
                encontrado = p
                break
        if encontrado:
            entry_nombre.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            entry_precio.delete(0, tk.END)

            entry_nombre.insert(0, encontrado.get_nombre())
            entry_cantidad.insert(0, str(encontrado.get_cantidad()))
            entry_precio.insert(0, str(encontrado.get_precio()))
            messagebox.showinfo("Producto encontrado", f"Producto con ID {pid} cargado en el formulario.")
        else:
            messagebox.showerror("No encontrado", f"No existe ningún producto con ID {pid}.")

    def guardar():
        inv.guardar_en_archivo()
        messagebox.showinfo("Guardado", "Inventario guardado exitosamente.")

    def salir():
        guardar()
        ventana.destroy()

    # ------- BOTONES -------
    frame_botones = tk.Frame(ventana, bg="white")
    frame_botones.pack(pady=10)

    # Botones principales
    botones = [
        ("Agregar", "#004aad", agregar),
        ("Modificar", "#ff9800", modificar),
        ("Eliminar", "#d32f2f", eliminar),
        ("Guardar", "#00796b", guardar),
        ("Salir", "#9e9e9e", salir)
    ]

    for i, (texto, color, accion) in enumerate(botones):
        tk.Button(
            frame_botones, text=texto, bg=color, fg="white",
            font=("Segoe UI", 11, "bold"), width=12, command=accion,
            relief="flat", cursor="hand2"
        ).grid(row=0, column=i, padx=10)

    # Botones pequeños adicionales
    tk.Button(frame_form, text="Limpiar campos", bg="#9e9e9e", fg="white",
              font=("Segoe UI", 10, "bold"), command=limpiar_campos,
              relief="flat", cursor="hand2").grid(row=0, column=2, rowspan=2, padx=10)

    tk.Button(frame_form, text="Buscar por ID", bg="#2196f3", fg="white",
              font=("Segoe UI", 10, "bold"), command=buscar_por_id,
              relief="flat", cursor="hand2").grid(row=0, column=3, rowspan=2, padx=10)

    actualizar_tabla()
    ventana.mainloop()


# -------- EJECUCIÓN --------
if __name__ == "__main__":
    mostrar_portada()
