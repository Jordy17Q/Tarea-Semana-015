import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Lista para almacenar las tareas
        self.tasks = []

        # --- Interfaz Gráfica ---
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Evento Enter

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.mark_completed)  # Doble clic

    # --- Lógica de la Aplicación ---
    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor escribe una tarea.")

    def mark_completed(self, event=None):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task = self.listbox.get(index)
            if not task.startswith("✔️ "):
                self.listbox.delete(index)
                self.listbox.insert(index, "✔️ " + task)
                self.listbox.itemconfig(index, fg="gray")
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminarla.")

# --- Ejecución ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()