import tkinter as tk
from tkinter import messagebox

# --- window setup ---
root = tk.Tk()
root.title("GUI Addition")
root.geometry("600x320")            # wider so the form looks good
root.resizable(False, False)

# --- fonts / common options ---
LABEL_FONT = ("Arial", 12)
ENTRY_FONT = ("Arial", 14)
RESULT_FONT = ("Arial", 14, "bold")

# --- form widgets ---
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill="both", expand=True)

# First number
lbl1 = tk.Label(frame, text="Enter The First Number:", font=LABEL_FONT, anchor="w")
lbl1.grid(row=0, column=0, sticky="w", pady=8)
entry1 = tk.Entry(frame, font=ENTRY_FONT, width=18)
entry1.grid(row=0, column=1, padx=12, pady=8)

# Second number
lbl2 = tk.Label(frame, text="Enter The Second Number:", font=LABEL_FONT, anchor="w")
lbl2.grid(row=1, column=0, sticky="w", pady=8)
entry2 = tk.Entry(frame, font=ENTRY_FONT, width=18)
entry2.grid(row=1, column=1, padx=12, pady=8)

# Result label (static part and dynamic part)
lbl_result_text = tk.Label(frame, text="Result:", font=LABEL_FONT)
lbl_result_text.grid(row=2, column=0, sticky="w", pady=14)
lbl_result_value = tk.Label(frame, text="", font=RESULT_FONT, fg="red")
lbl_result_value.grid(row=2, column=1, sticky="w", pady=14)

# Button action
def do_addition():
    a = entry1.get().strip()
    b = entry2.get().strip()
    if a == "" or b == "":
        messagebox.showinfo("Input required", "Please enter both numbers.")
        return
    try:
        # try to parse as float so decimals work; if you only want integers use int()
        va = float(a)
        vb = float(b)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
        return

    s = va + vb
    # display as int when it's whole, otherwise show float with up to 6 decimals
    if s.is_integer():
        s = int(s)
    else:
        s = round(s, 6)

    lbl_result_value.config(text=str(s))

# Submit button
btn = tk.Button(frame, text="Submit", command=do_addition,
                font=("Arial", 12, "bold"), bg="#f0f0f0", padx=12, pady=6)
btn.grid(row=3, column=0, columnspan=2, pady=10)

# Keep columns sized nicely
frame.grid_columnconfigure(0, weight=0, minsize=220)
frame.grid_columnconfigure(1, weight=1)

root.mainloop()
