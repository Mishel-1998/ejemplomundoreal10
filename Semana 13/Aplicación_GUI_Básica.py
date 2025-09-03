import tkinter as tk
from tkinter import messagebox

# ===============================
#   Aplicación GUI con Tkinter
# ===============================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos - Ejemplo GUI con Tkinter")
        self.root.geometry("400x300")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)

        # Botones
        self.btn_add = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.btn_add.pack(pady=5)

        self.btn_clear = tk.Button(root, text="Limpiar", command=self.limpiar_dato)
        self.btn_clear.pack(pady=5)

        # Lista
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

    # Función para agregar datos
    def agregar_dato(self):
        dato = self.entry.get().strip()
        if dato:  # Verifica que no esté vacío
            self.listbox.insert(tk.END, dato)
            self.entry.delete(0, tk.END)  # Limpia el campo
        else:
            messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

    # Función para limpiar datos
    def limpiar_dato(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            self.listbox.delete(seleccion)  # Borra el seleccionado
        else:
            confirm = messagebox.askyesno("Confirmar", "¿Desea limpiar toda la lista?")
            if confirm:
                self.listbox.delete(0, tk.END)  # Borra todo

# ===============================
#   Inicializar la aplicación
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
