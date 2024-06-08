import tkinter as tk
from tkinter import Frame, Label, Button, ttk
from calculator import main

ent_customer_amount = None

#choises= ["Asado", "Hamburger","Fried chicken"]
def main_change_calculator():
    global frm_change_calculator
    
    root = tk.Tk()
    root.geometry("200x200")
    frm_change_calculator= Frame(root)
    frm_change_calculator.master.title("Calculator")
    frm_change_calculator.pack(padx=5, pady=3, fill=tk.BOTH, expand=1)
    frm_change_calculator.config(bg= 'lightblue')

    populate_main_window(frm_change_calculator)

    root.mainloop()

def populate_main_window(frm_change_calculator):
    options = {
      'fried chicken': 12,
      'Asado': 15,
      'Hamburguer': 10
    }

    def dish(*args):
        item_price = options.get(clicked.get(), 0)  
        try:
            money_got = float(ent_customer_amount.get()) 
        except ValueError:
            money_got = 0
        result = money_got - item_price
        lbl_screen_price.config(text=f"Change: ${result:.2f}")  

    global clicked, ent_customer_amount, lbl_screen_price
    clicked = tk.StringVar(frm_change_calculator)

    clicked.trace_variable('w', dish)


    clicked.set("Chose a dish")
    lbl_welcome_text = Label(frm_change_calculator, text= "Calculate Valance",width=20 , bg= 'lightblue')
    drop_down= tk.OptionMenu(frm_change_calculator, clicked, *options.keys()  )

    lbl_customer_amount= Label(frm_change_calculator, anchor='w', text='Amount recived', width=15 , bg= 'lightblue')
    lbl_singn1= Label(frm_change_calculator, text="$" , bg= 'lightblue', anchor="w")
    ent_customer_amount= tk.Entry(frm_change_calculator, width=15 )
    lbl_change= Label(frm_change_calculator, anchor='w', text="Change", width=15 , bg= 'lightblue')
    lbl_screen_price = Label(frm_change_calculator, anchor= 'w', text="", width=15 , bg= 'lightblue')
    btn_calculator= Button(frm_change_calculator, text="Calculator",command=lambda:main())

    space= Label(frm_change_calculator, text="", bg="lightblue")
    space1= Label(frm_change_calculator, text="", bg="lightblue")

    lbl_welcome_text.grid( row = 2, column=1)
    drop_down.grid(row=3, column=1)
    lbl_customer_amount.grid(row=5,column=1)
    lbl_singn1.grid(row=6, column=2)
    ent_customer_amount.grid(row=6, column=1)
    lbl_change.grid(row=7, column=1)

    space1.grid(row=0)
    #space3.grid(row=3)
    space.grid(row=7)
    btn_calculator.grid(row=9, column=1)

def show():
    global frm_change_calculator, clicked, lbl_screen_price
    
    lbl_screen_price.config(text=clicked.get())

    

#def get_price_from_list():

 #   global choises, lbl_screen_price

 #  if :
 #       lbl_screen_price.config(text="10") 
  #  else: 
    #    lbl_screen_price.config(text="15")









   
if __name__=="__main__":
    main_change_calculator() 