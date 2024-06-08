import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
from number_entry import IntEntry

def main(): 
    root = tk.Tk()
    root.geometry("400x500")
    frm_main = Frame(root)
    frm_main.master.title("Calculator")
    frm_main.pack(padx=5, pady=3, fill=tk.BOTH, expand=1)

    populate_main_window(frm_main)

    root.mainloop()

def populate_main_window(frm_main):
    # Create a FloatEntry widget for displaying the input
    ent_screen = FloatEntry(frm_main, width=6)
    ent_screen.grid(row=0, column=3, padx=3, pady=1)
    
    # Define functions for calculator operations
    def add_to_screen(value):
        current_value = ent_screen.get()
        ent_screen.delete(0, tk.END)
        ent_screen.insert(0, str(current_value) + str(value))
    
    def clear_screen():
        ent_screen.delete(0, tk.END)
    
    def calculate():
        expression = ent_screen.get()
        try:
            result = eval(expression)
            ent_screen.delete(0, tk.END)
            ent_screen.insert(0, str(result))
        except Exception as e:
            ent_screen.delete(0, tk.END)
            ent_screen.insert(0, "Error")

    # Create buttons for calculator operations
    buttons = [
        (" C ", clear_screen),
        (" +/- ", None),
        (" % ", None),
        (" ÷ ", lambda: add_to_screen("/")),
        (" 7 ", lambda: add_to_screen("7")),
        (" 8 ", lambda: add_to_screen("8")),
        (" 9 ", lambda: add_to_screen("9")),
        (" x ", lambda: add_to_screen("*")),
        (" 4 ", lambda: add_to_screen("4")),
        (" 5 ", lambda: add_to_screen("5")),
        (" 6 ", lambda: add_to_screen("6")),
        (" - ", lambda: add_to_screen("-")),
        (" 1 ", lambda: add_to_screen("1")),
        (" 2 ", lambda: add_to_screen("2")),
        (" 3 ", lambda: add_to_screen("3")),
        (" + ", lambda: add_to_screen("+")),
        (" 0 ", lambda: add_to_screen("0")),
        (" . ", lambda: add_to_screen(".")),
        (" = ", calculate)
    ]

    # Place buttons in the window
    row = 1
    col = 0
    for text, command in buttons:
        btn = Button(frm_main, text=text, command=command)
        btn.grid(row=row, column=col, padx=2, pady=1)
        col += 1
        if col > 3:
            col = 0
            row += 1

if __name__ == "__main__":
    main()