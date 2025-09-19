import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # --- Entrada de texto para nueva tarea ---
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Permitir Enter

        # --- Botones de acciones ---
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # --- Lista de tareas ---
        self.task_listbox = tk.Listbox(self.root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Doble clic en tarea para marcar como completada
        self.task_listbox.bind("<Double-1>", self.complete_task)

    # --- Función para añadir tarea ---
    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Escribe una tarea antes de añadir.")

    # --- Función para marcar tarea como completada ---
    def complete_task(self, event=None):
        try:
            index = self.task_listbox.curselection()[0]  # Índice de la tarea seleccionada
            task = self.task_listbox.get(index)

            # Si ya tiene marca, la quitamos, si no la añadimos
            if task.startswith("✔ "):
                task = task[2:]  # Quitar marca
            else:
                task = "✔ " + task  # Añadir marca

            self.task_listbox.delete(index)
            self.task_listbox.insert(index, task)
        except IndexError:
            messagebox.showwarning("Selección Vacía", "Selecciona una tarea para completar.")

    # --- Función para eliminar tarea ---
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Selección Vacía", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
