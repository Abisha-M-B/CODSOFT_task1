import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'Please enter a task.')


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning('Warning', 'Please select a task to delete.')


# Create the main window
root = tk.Tk()
root.title('To-Do List')

# Create the task entry box
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create the listbox
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack()

# Create buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

button_add_task = tk.Button(frame_buttons, text='Add Task', width=10, command=add_task, fg="white", bg="maroon")
button_add_task.grid(row=0, column=0, padx=5)

button_delete_task = tk.Button(frame_buttons, text='Delete Task', width=10, command=delete_task, fg="white", bg="maroon")
button_delete_task.grid(row=0, column=1, padx=5)

# Run the main loop
root.mainloop()
