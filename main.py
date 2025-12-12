import tkinter as tk
from tkinter import messagebox
import calculator  # Importing the student's work

def run_calculation(operation_name):
    """
    Helper function to safely call functions from calculator.py
    even if they haven't been implemented yet.
    """
    # 1. Get Inputs
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    # 2. Check if function exists in calculator.py
    # We look for the function by name (e.g., 'add', 'subtract')
    func = getattr(calculator, operation_name, None)

    if func is None:
        messagebox.showwarning("Not Implemented", f"The function '{operation_name}' is missing!\n\nGo into calculator.py and add it.")
        return

    # 3. Execute and Show Result
    try:
        result = func(val1, val2)
        label_result.config(text=f"Result: {result}", fg="green")
    except Exception as e:
        messagebox.showerror("Execution Error", f"Something went wrong running {operation_name}:\n{str(e)}")

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Class Calculator Project")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# Title
tk.Label(root, text="Python Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

# Inputs
frame_inputs = tk.Frame(root, bg="#f0f0f0")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Number 1:", bg="#f0f0f0").grid(row=0, column=0, padx=5)
entry_num1 = tk.Entry(frame_inputs, font=("Arial", 12), width=10)
entry_num1.grid(row=0, column=1, padx=5)

tk.Label(frame_inputs, text="Number 2:", bg="#f0f0f0").grid(row=1, column=0, padx=5)
entry_num2 = tk.Entry(frame_inputs, font=("Arial", 12), width=10)
entry_num2.grid(row=1, column=1, padx=5)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=20)

# Helper to create buttons
def create_btn(text, func_name, row, col, color="#e1e1e1"):
    btn = tk.Button(frame_buttons, text=text, font=("Arial", 12), width=10, bg=color,
                    command=lambda: run_calculation(func_name))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Row 1
create_btn("Add (+)", "add", 0, 0, "#d1e7dd")       # Already works
create_btn("Subtract (-)", "subtract", 0, 1)        # Needs Implementation

# Row 2
create_btn("Multiply (*)", "multiply", 1, 0)        # Needs Implementation
create_btn("Divide (/)", "divide", 1, 1)            # Needs Implementation

# Row 3
create_btn("Modulo (%)", "modulo", 2, 0)            # Needs Implementation

# Result Label
label_result = tk.Label(root, text="Result: ---", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
label_result.pack(pady=20)

# Instructions
tk.Label(root, text="Edit calculator.py to make buttons work!", font=("Arial", 10, "italic"), bg="#f0f0f0", fg="#666").pack(side="bottom", pady=10)

root.mainloop()
