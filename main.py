import sys
import calculator 

try:
    import tkinter as tk
    from tkinter import messagebox
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

def run_calculation_logic(operation_name, n1, n2):
    """
    Core logic to call functions from calculator.py safely.
    Returns (Success: bool, Result/Message: str)
    """
    # Check if function exists in calculator.py
    func = getattr(calculator, operation_name, None)

    if func is None:
        return False, f"Not Implemented: The function '{operation_name}' is missing in calculator.py"

    try:
        result = func(n1, n2)
        return True, result
    except Exception as e:
        return False, f"Execution Error: {str(e)}"

# --- GUI MODE ---
def run_gui():
    def on_click(operation_name):
        try:
            val1 = float(entry_num1.get())
            val2 = float(entry_num2.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return

        success, output = run_calculation_logic(operation_name, val1, val2)
        
        if success:
            label_result.config(text=f"Result: {output}", fg="green")
        else:
            if "Not Implemented" in output:
                messagebox.showwarning("Missing Function", output)
            else:
                messagebox.showerror("Error", output)

    root = tk.Tk()
    root.title("Class Calculator Project")
    root.geometry("400x450")
    root.configure(bg="#f0f0f0")

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

    # Buttons
    frame_buttons = tk.Frame(root, bg="#f0f0f0")
    frame_buttons.pack(pady=20)

    def create_btn(text, func_name, row, col, color="#e1e1e1"):
        btn = tk.Button(frame_buttons, text=text, font=("Arial", 12), width=10, bg=color,
                        command=lambda: on_click(func_name))
        btn.grid(row=row, column=col, padx=5, pady=5)

    create_btn("Add (+)", "add", 0, 0, "#d1e7dd")
    create_btn("Subtract (-)", "subtract", 0, 1)
    create_btn("Multiply (*)", "multiply", 1, 0)
    create_btn("Divide (/)", "divide", 1, 1)
    create_btn("Modulo (%)", "modulo", 2, 0)

    label_result = tk.Label(root, text="Result: ---", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
    label_result.pack(pady=20)
    
    root.mainloop()

# --- CLI MODE (Fallback) ---
def run_cli():
    print("\n" + "="*40)
    print("WARNING: Tkinter not found. Running in Text Mode.")
    print("="*40)
    print("Available operations: add, subtract, multiply, divide, modulo")
    print("Type 'q' to quit.\n")

    while True:
        op = input("Enter operation: ").strip().lower()
        if op == 'q': break
        
        try:
            n1 = float(input("Number 1: "))
            n2 = float(input("Number 2: "))
            
            success, output = run_calculation_logic(op, n1, n2)
            
            if success:
                print(f"✅ Result: {output}")
            else:
                print(f"❌ {output}")
            print("-" * 20)
            
        except ValueError:
            print("❌ Error: Please enter valid numbers.")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    if GUI_AVAILABLE:
        run_gui()
    else:
        run_cli()