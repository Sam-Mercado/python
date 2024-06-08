# Copyright 2020, Brigham Young University-Idaho. All rights reserved.
 
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
 
 
def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.master.title("Calculate the area")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
 
    populate_main_window(frm_main)
 
    root.mainloop()

 
def populate_main_window(frm_main):
   
    lbl_w = Label(frm_main, text="Enter Width")
    ent_w = FloatEntry(frm_main, width=4)
    
    lbl_h = Label(frm_main, text="Enter Height")
    ent_h = FloatEntry(frm_main, width=4)
    
    lbl_area_i = Label(frm_main, text="Area:")
    lbl_area = Label(frm_main, width=5)
    lbl_square_units = Label(frm_main, text="square units")
    btn_clear = Button(frm_main, text="Clear")
 
    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_w.grid(      row=0, column=0, padx=3, pady=3)
    ent_w.grid(      row=0, column=1, padx=3, pady=3)
    lbl_h.grid(      row=0, column=2, padx=3, pady=3)
    ent_h.grid(      row=0, column=3, padx=3, pady=3)
  
 
    lbl_area_i.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_area.grid(      row=1, column=1, padx=3, pady=3)
    lbl_square_units.grid(row=1, column=3, padx=0, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")
 
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            width = int(ent_w.get())
            height = int(ent_h.get())
 
            area = width * height
 
            lbl_area.config(text=f"{area:.0f}")
 
        except ValueError:
            lbl_area.config(text="Invalid")
          
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_w.clear()
        ent_h.clear()
        lbl_area.config(text="")
        ent_w.focus()
 
    ent_w.bind("<KeyRelease>", calculate)
    ent_h.bind("<KeyRelease>", calculate)
 

    btn_clear.config(command=clear)
 
    ent_w.focus()
    ent_h.focus()
 
if __name__ == "__main__":
    main()
 