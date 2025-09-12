"""
agenda_tkinter.py
Aplicación de Agenda Personal con Tkinter y DatePicker (tkcalendar)

- Treeview para mostrar eventos (fecha, hora, descripción)
- Campos de entrada: DateEntry (calendario), hora (Entry), descripción (Entry)
- Botones: Agregar, Eliminar seleccionado, Salir
- Confirmación al eliminar
- Organización con Frames
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from tkcalendar import DateEntry   # ahora SIEMPRE se usa

# ---------- Aplicación principal ----------
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # Frames principales
        self.frame_list = ttk.Frame(self.root, padding=(10, 10))
        self.frame_list.grid(row=0, column=0, sticky="nsew")

        self.frame_inputs = ttk.Frame(self.root, padding=(10, 0))
        self.frame_inputs.grid(row=1, column=0, sticky="ew")

        self.frame_actions = ttk.Frame(self.root, padding=(10, 10))
        self.frame_actions.grid(row=2, column=0, sticky="ew")

        # Inicializar componentes
        self._create_treeview()
        self._create_input_fields()
        self._create_action_buttons()

        self._next_id = 1  # contador interno

    # --- Treeview de eventos ---
    def _create_treeview(self):
        label = ttk.Label(self.frame_list, text="Eventos programados", font=("Segoe UI", 11, "bold"))
        label.pack(anchor="w", pady=(0,6))

        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_list, columns=columns, show="headings", height=12)
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=100, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", width=460, anchor="w")

        vsb = ttk.Scrollbar(self.frame_list, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

    # --- Campos de entrada ---
    def _create_input_fields(self):
        sub = ttk.Frame(self.frame_inputs)
        sub.pack(fill="x", expand=True)

        # Fecha con DateEntry
        lbl_fecha = ttk.Label(sub, text="Fecha:")
        lbl_fecha.grid(row=0, column=0, sticky="w", padx=(0,6), pady=(6,6))
        self.entry_fecha = DateEntry(sub, date_pattern='dd/mm/yyyy', width=12)
        self.entry_fecha.grid(row=0, column=1, sticky="w", pady=(6,6))

        # Hora
        lbl_hora = ttk.Label(sub, text="Hora (HH:MM, 24h):")
        lbl_hora.grid(row=0, column=2, sticky="w", padx=(12,6), pady=(6,6))
        self.entry_hora = ttk.Entry(sub, width=10)
        self.entry_hora.insert(0, "09:00")
        self.entry_hora.grid(row=0, column=3, sticky="w", pady=(6,6))

        # Descripción
        lbl_desc = ttk.Label(sub, text="Descripción:")
        lbl_desc.grid(row=1, column=0, sticky="w", padx=(0,6), pady=(6,6))
        self.entry_desc = ttk.Entry(sub, width=60)
        self.entry_desc.grid(row=1, column=1, columnspan=3, sticky="w", pady=(6,6))

        sub.grid_columnconfigure(1, weight=1)

    # --- Botones ---
    def _create_action_buttons(self):
        btn_agregar = ttk.Button(self.frame_actions, text="Agregar Evento", command=self.agregar_evento)
        btn_agregar.pack(side="left", padx=(0,6))

        btn_eliminar = ttk.Button(self.frame_actions, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_eliminar.pack(side="left", padx=(6,6))

        btn_salir = ttk.Button(self.frame_actions, text="Salir", command=self.salir)
        btn_salir.pack(side="right", padx=(6,0))

    # --- Agregar evento ---
    def agregar_evento(self):
        fecha_str = self.entry_fecha.get().strip()
        hora_str = self.entry_hora.get().strip()
        desc = self.entry_desc.get().strip()

        if not fecha_str or not hora_str or not desc:
            messagebox.showwarning("Campos incompletos", "Completa fecha, hora y descripción.")
            return

        # Validar fecha
        try:
            fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
            fecha_ok = fecha_obj.strftime("%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Fecha inválida", "Usa formato dd/mm/yyyy.")
            return

        # Validar hora
        try:
            hora_obj = datetime.strptime(hora_str, "%H:%M")
            hora_ok = hora_obj.strftime("%H:%M")
        except ValueError:
            messagebox.showerror("Hora inválida", "Usa formato HH:MM (24h).")
            return

        # Insertar en Treeview
        iid = f"event_{self._next_id}"
        self.tree.insert("", "end", iid=iid, values=(fecha_ok, hora_ok, desc))
        self._next_id += 1

        # Limpiar campos
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    # --- Eliminar evento ---
    def eliminar_evento(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Selecciona un evento", "Selecciona un evento en la lista.")
            return

        if len(selected) == 1:
            msg = "¿Eliminar el evento seleccionado?"
        else:
            msg = f"¿Eliminar los {len(selected)} eventos seleccionados?"

        if not messagebox.askyesno("Confirmar", msg):
            return

        for item in selected:
            self.tree.delete(item)

    # --- Salir ---
    def salir(self):
        self.root.quit()


# ---------- Main ----------
def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('default')
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
