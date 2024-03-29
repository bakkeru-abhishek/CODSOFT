import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.tasks = []

        # Styling
        self.master.configure(bg='#F0F0F0')
        self.frame = tk.Frame(master, bg='#F0F0F0')
        self.frame.pack(expand=True)

        # Entry for adding tasks
        self.task_entry = ttk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Add Task button
        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Show Tasks button
        self.show_button = ttk.Button(self.frame, text="Show Tasks", command=self.show_tasks)
        self.show_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Frame for displaying tasks
        self.task_frame = tk.Frame(self.frame, bg='#D3D3D3')
        self.task_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Listbox for displaying tasks
        self.listbox = tk.Listbox(self.task_frame, width=50)
        self.listbox.pack()

        # Delete Task button
        self.delete_button = ttk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, padx=10, pady=10)

        # Exit button
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task added successfully!")

    def delete_task(self):
        try:
            selection = self.listbox.curselection()
            if selection:
                index = selection[0]
                self.listbox.delete(index)
                del self.tasks[index]
                messagebox.showinfo("Success", "Task deleted successfully!")
        except IndexError:
            pass

    def show_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
