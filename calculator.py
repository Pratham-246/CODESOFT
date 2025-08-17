import tkinter as tk

def click(btn_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + btn_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#ffe5b4")

entry = tk.Entry(root, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify="right")
entry.pack(pady=20, padx=10, fill="x")

btn_frame = tk.Frame(root, bg="#ffe5b4")
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(btn_frame, bg="#ffe5b4")
    row_frame.pack(pady=5)
    for btn in row:
        color = "#bc4749" if btn in "+-*/" else "#588157" if btn == "=" else "#f77f00"
        b = tk.Button(row_frame, text=btn, width=6, height=2, font=("Arial", 14),
                      bg=color, fg="white", command=lambda b=btn: calculate() if b == "=" else click(b))
        b.pack(side="left", padx=5)

clr_btn = tk.Button(root, text="Clear", font=("Arial", 14), bg="#3a5a40", fg="white",
                    width=28, height=2, command=clear)
clr_btn.pack(pady=15)

root.mainloop()
