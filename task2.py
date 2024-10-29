import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.config(bg="#333")  
        self.current_input = ""
        
        self.display = tk.Entry(root, font=("Helvetica", 18, "bold"), borderwidth=2, relief="solid", justify="right", bg="#222", fg="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+' 
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, width=5, height=2, command=action, font=("Helvetica", 14), 
                      bg="#444", fg="white", activebackground="#666", activeforeground="white").grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        clear_button = tk.Button(root, text="C", width=22, height=2, command=self.clear_display, 
                                 font=("Helvetica", 14, "bold"), bg="red", fg="white", activebackground="#aa0000")
        clear_button.grid(row=row, column=0, columnspan=4, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.current_input)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.current_input = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif char == "C":
            self.clear_display()
        else:
            self.current_input += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.current_input)

    def clear_display(self):
        self.current_input = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
