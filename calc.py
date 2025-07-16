import tkinter as tk

def show_calculator():
    
    calc_window = tk.Toplevel(root)
    calc_window.title("Calculator")
    calc_window.geometry("300x400")

    entry = tk.Entry(calc_window, font="Arial 20")
    entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

    def click(event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = str(eval(entry.get()))
                entry.delete(0, tk.END)
                entry.insert(0, result)
            except:
                entry.delete(0, tk.END)
                entry.insert(0, "Error")
        elif text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, text)

    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['C', '0', '=', '+']
    ]

    for row in buttons:
        frame = tk.Frame(calc_window)
        frame.pack(expand=True, fill="both")
        for btn_text in row:
            btn = tk.Button(frame, text=btn_text, font="Arial 18", relief='ridge')
            btn.pack(side="left", expand=True, fill="both")
            btn.bind("<Button-1>", click)

root = tk.Tk()
root.title("Main Page")
root.geometry("300x200")

welcome_label = tk.Label(root, text="Welcome to Output Page", font="Arial 16")
welcome_label.pack(pady=20)

open_calc_btn = tk.Button(root, text="Open Calculator", font="Arial 14", command=show_calculator)
open_calc_btn.pack(pady=20)

root.mainloop()