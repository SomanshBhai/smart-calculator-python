import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Smart Calculator")
root.geometry("400x300")

def open_calculator(operation):
    
    calc_window = tk.Toplevel(root)

    operation_names = {
        "+": "Addition",
        "-": "Subtraction",
        "*": "Multiplication",
        "/": "Division"
    }

    calc_window.title(operation_names[operation])
    calc_window.geometry("350x250")

    tk.Label(calc_window, text="Enter First Number").pack(pady=5)
    num1_entry = tk.Entry(calc_window)
    num1_entry.pack()

    tk.Label(calc_window, text="Enter Second Number").pack(pady=5)
    num2_entry = tk.Entry(calc_window)
    num2_entry.pack()

    result_label = tk.Label(calc_window, text="Solution: ", font=("Arial", 12, "bold"))
    result_label.pack(pady=15)

    def solve():
        try:
            num1 = float(num1_entry.get())
            num2 = float(num2_entry.get())

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = num1 / num2

            result_label.config(text=f"Solution: {result}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

    tk.Button(
        calc_window,
        text="Solve",
        font=("Arial", 12),
        command=solve
    ).pack(pady=10)


tk.Label(
    root,
    text="SMART CALCULATOR",
    font=("Arial", 18, "bold")
).pack(pady=20)


tk.Button(root, text="Addition", width=20,
          command=lambda: open_calculator("+")).pack(pady=5)

tk.Button(root, text="Subtraction", width=20,
          command=lambda: open_calculator("-")).pack(pady=5)

tk.Button(root, text="Multiplication", width=20,
          command=lambda: open_calculator("*")).pack(pady=5)

tk.Button(root, text="Division", width=20,
          command=lambda: open_calculator("/")).pack(pady=5)

root.mainloop()