import tkinter as tk

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

def clear_all():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.config(bg="#fefae0")

title = tk.Label(root, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#fefae0", fg="#3a5a40")
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=25)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", font=("Helvetica", 12), bg="#588157", fg="white", width=15, command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Helvetica", 14), width=30, height=10)
listbox.pack(pady=10)

del_btn = tk.Button(root, text="Delete Selected", font=("Helvetica", 12), bg="#bc4749", fg="white", width=15, command=delete_task)
del_btn.pack(pady=5)

clr_btn = tk.Button(root, text="Clear All", font=("Helvetica", 12), bg="#f77f00", fg="white", width=15, command=clear_all)
clr_btn.pack(pady=5)

root.mainloop()
