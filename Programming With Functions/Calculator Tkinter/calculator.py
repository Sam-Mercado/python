import tkinter as tk
from tkinter import Frame, Label, Button


equation = ""
def main(): 

    root = tk.Tk()
    root.geometry("430x300")
    frm_main = Frame(root)
    frm_main.master.title("Calculator")
    frm_main.pack(padx=5, pady=3, fill=tk.BOTH, expand=1)
    frm_main.config(bg="#2C3E50")

    populate_main_window_calculator(frm_main)

    root.mainloop()

def populate_main_window_calculator(frm_main):
    global lbl_screen
    
    #row 1 buttons
    space= Label(frm_main, width=20,height = 2, text="", bg="#2C3E50")
    space2= Label(frm_main, width=20,height = 1, text="", bg="#2C3E50")
    lbl_screen = Label(frm_main, width=55,height = 2, text="")
    

    btn_porsentage = Button(frm_main, text=" % " , height= 2, width= 10, bg="#E74C3C", command=lambda: display_in_screen(" % "))
    btn_open_parentesis = Button(frm_main, text=" ( " , height= 2, width= 10, bg="#E74C3C",command=lambda: display_in_screen(" ( "))
    btn_close_parentesis = Button(frm_main, text=" ) " , height= 2, width= 10, bg="#E74C3C", command=lambda: display_in_screen(" ) "))
    btn_delete = Button(frm_main, text=" C ", height= 2, width= 10, bg="#E67E22",command=lambda: delete_from_screen())


    btn_multiplication = Button(frm_main, height= 2, width= 10, text=" x ", bg= "#3498DB", command=lambda: display_in_screen("*"))
    btn_division= Button(frm_main, text=" ÷ ", height= 2, width= 10, bg= "#3498DB", command=lambda: display_in_screen("/"))
    btn_substraction = Button(frm_main, text=" - ", height= 2, width= 10, bg= "#3498DB", command=lambda: display_in_screen(" - ") )
    btn_sum = Button(frm_main, text=" + " , height= 2, width= 10 , bg= "#3498DB", command=lambda: display_in_screen(" + "))
    

    
    
    #row2 buttons
    btn_7 = Button(frm_main, text=" 7 ",height= 2, width= 10, command=lambda: display_in_screen("7"))
    btn_8 = Button(frm_main, text=" 8 ", height= 2, width= 10, command=lambda: display_in_screen("8"))
    btn_9 = Button(frm_main, text=" 9 ", height= 2, width= 10, command=lambda: display_in_screen("9"))
   

    btn_4 = Button(frm_main, text=" 4 ", height= 2, width= 10, command=lambda: display_in_screen("4") )
    btn_5 = Button(frm_main, text=" 5 ", height= 2, width= 10, command=lambda: display_in_screen("5") )
    btn_6 = Button(frm_main, text=" 6 ", height= 2, width= 10, command=lambda: display_in_screen("6") )
    

    btn_1 = Button(frm_main, text=" 1 ", height= 2, width= 10, command=lambda: display_in_screen("1") )
    btn_2 = Button(frm_main, text=" 2 ", height= 2, width= 10, command=lambda: display_in_screen("2") )
    btn_3 = Button(frm_main, text=" 3 ", height= 2, width= 10, command=lambda: display_in_screen("3") )
    

    btn_0 = Button(frm_main, text=" 0 ", height= 2, width= 10, command=lambda: display_in_screen("0"))
    btn_dot = Button( frm_main, text=" . ", height= 2, width= 10, command=lambda: display_in_screen("."))
    btn_equial = Button(frm_main, text= " = ", height= 2, width= 10, command=lambda: calculation())




    space.grid(row=0, columnspan=5)
    lbl_screen.grid(row=1, columnspan=5)
    space2.grid(row=2, columnspan=5)
 
    #row 2
    btn_7.grid(row=3, column=1, padx=2, pady=1)
    btn_8.grid(row=3, column=2, padx=2, pady=1)
    btn_9.grid(row=3, column=3, padx=2, pady=1)
    btn_multiplication.grid(row=3, column=4, padx=2, pady=1)
    btn_delete.grid(row=3, column=0, padx=2, pady=1)

    #row3
    btn_4.grid(row=4, column=1, padx=2, pady=1)
    btn_5.grid(row=4, column=2, padx=2, pady=1)
    btn_6.grid(row=4, column=3, padx=2, pady=1)
    btn_open_parentesis.grid(row=4, column=0, padx=2, pady=1)
    btn_division.grid(row=4, column=4, padx=2 , pady=1)
    #row 4 
    btn_1.grid(row=5, column=1, padx=2, pady=1)
    btn_2.grid(row=5, column=2, padx=2, pady=1)
    btn_3.grid(row=5, column=3, padx=2, pady=1)
    btn_substraction.grid(row=5, column=4, padx=2, pady=1)
    btn_close_parentesis.grid(row=5, column=0, padx=2, pady=1)
    
    #row 5 
    btn_0.grid(row=6, column=2, padx=2, pady=1)
    btn_dot.grid(row=6, column=1, padx=2, pady=1)
    btn_equial.grid(row=6, column=3, padx=2, pady=1)
    btn_sum.grid(row=6, column=4, padx=2, pady=1)
    btn_porsentage.grid(row=6, column=0, padx=2, pady=1)
     
def display_in_screen(value): 
    global equation,lbl_screen
    equation+=value
    lbl_screen.config(text=equation)

def delete_from_screen():
    global equation, lbl_screen
    equation=""
    lbl_screen.config(text=equation)

def calculation():
    global equation, lbl_screen
    if equation != "":
        try: 
            result= eval(equation)
        except: 
            result= "ERROR"
            equation = ""

    lbl_screen.config(text=result)

if __name__ =="__main__":
    main()