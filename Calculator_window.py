from tkinter import *
from tkinter import ttk



import Calculator_functions as calc

expression = ""

def get_index():
    return(entr.index(INSERT))

def btn_1_clicked():
    entr.insert(get_index(), "1")

def btn_2_clicked():
    entr.insert(get_index(), "2")

def btn_3_clicked():
    entr.insert(get_index(), "3")

def btn_4_clicked():
    entr.insert(get_index(), "4")

def btn_5_clicked():
    entr.insert(get_index(), "5")

def btn_6_clicked():
    entr.insert(get_index(), "6")

def btn_7_clicked():
    entr.insert(get_index(), "7")

def btn_8_clicked():
    entr.insert(get_index(), "8")

def btn_9_clicked():
    entr.insert(get_index(), "9")

def btn_0_clicked():
    entr.insert(get_index(), "0")

def btn_multiplication_clicked():
    entr.insert(get_index(), "*")

def btn_addition_clicked():
    entr.insert(get_index(), "+")

def btn_division_clicked():
    entr.insert(get_index(), "/")

def btn_substraction_clicked():
    entr.insert(get_index(), "-")

def btn_power_clicked():
    entr.insert(get_index(), "^")

def btn_right_bracket_clicked():
    entr.insert(get_index(), ")")

def btn_left_bracket_clicked():
    entr.insert(get_index(), "(")

def btn_delete_clicked():
    entr.delete(first=get_index()-1, last=None)

def btn_clear_clicked():
    entr.delete(first=0, last = END)

def btn_dot_clicked():
    entr.insert(get_index(), ".")

def btn_equal_clicked():
    global expression
    expression=entr.get()
    calc.complex_converter()
    while "(" in expression:
        left_index, right_index = calc.bracket_finder()
        calc.bracket_calc(left_index, right_index)
    while len(expression)>1:
        calc.main_calc()
    expression = expression[0]
    if expression.imag == 0j:
        expression = expression.real
    entr.insert(END, f"={expression}")




window = Tk()
window.title("Calculator")
window.geometry("480x350")
# lbl = Label(window, text = "test", font = ("Times New Roman", 14))
# lbl.grid(column=1, row=0)
# btn = Button(window, text = "Test", font = ("Times New Roman", 12))
# btn.grid(column = 1, row = 1)
# btn2 = Button(window, text = "Test2", font = ("Times New Roman", 12), bg="grey", fg="white", command = btn2_test)
# btn2.grid(column = 0, row = 1)
# txt = Entry(window, width=10)
# txt.grid(column=0, row=0)
# txt.focus()
entr = ttk.Entry(window)
entr.place(x=1, y=1, width=239, height=40)
btn_1 = ttk.Button(window,text = "1", command=btn_1_clicked)
btn_1.place(x=1, y= 121,width=80, height=80)
btn_2=ttk.Button(window, text = "2", command=btn_2_clicked)
btn_2.place(x=81, y= 121,width=80, height=80)
btn_3=ttk.Button(window, text = "3", command=btn_3_clicked)
btn_3.place(x=161, y= 121,width=80, height=80)
btn_4=ttk.Button(window, text = "4", command=btn_4_clicked)
btn_4.place(x=1, y= 201,width=80, height=80)
btn_5 = ttk.Button(window, text = "5", command=btn_5_clicked)
btn_5.place(x=81, y= 201,width=80, height=80)
btn_6=ttk.Button(window, text="6", command=btn_6_clicked)
btn_6.place(x=161, y= 201,width=80, height=80)
btn_7 = ttk.Button(window, text = "7", command=btn_7_clicked)
btn_7.place(x=1, y= 281,width=80, height=80)
btn_8 = ttk.Button(window, text = "8", command=btn_8_clicked)
btn_8.place(x=81, y=281,width=80, height=80)
btn_9 = ttk.Button(window, text = "9", command=btn_9_clicked)
btn_9.place(x=161, y= 281,width=80, height=80)
btn_clear = ttk.Button(window, text = "C", command=btn_clear_clicked)
btn_clear.place(x=1,y = 41, width = 80, height=80)
btn_left_bracket = ttk.Button(window, text = "(", command=btn_left_bracket_clicked)
btn_left_bracket.place(x=81,y = 41, width = 80, height=80)
btn_right_bracket = ttk.Button(window, text = ")", command=btn_right_bracket_clicked)
btn_right_bracket.place(x=161,y = 41, width = 80, height=80)
btn_multiplication = ttk.Button(window, text = "*", command=btn_multiplication_clicked)
btn_multiplication.place(x=241,y = 41, width = 80, height=80)
btn_division = ttk.Button(window, text = "/", command=btn_division_clicked)
btn_division.place(x=241,y = 121, width = 80, height=80)
btn_addition = ttk.Button(window, text = "+", command=btn_addition_clicked)
btn_addition.place(x=241,y = 201, width = 80, height=80)
btn_substraction = ttk.Button(window, text = "-", command=btn_substraction_clicked)
btn_substraction.place(x=241,y = 281, width = 80, height=80)
btn_dot = ttk.Button(window, text = ".", command=btn_dot_clicked)
btn_dot.place(x=1,y = 361, width = 80, height=80)
btn_0 = ttk.Button(window, text = "0", command=btn_0_clicked)
btn_0.place(x=81,y = 361, width = 80, height=80)
btn_power = ttk.Button(window, text = "^", command=btn_power_clicked)
btn_power.place(x=161,y = 361, width = 80, height=80)
btn_equal = ttk.Button(window, text = "=", command=btn_equal_clicked)
btn_equal.place(x=241,y = 361, width = 80, height=80)
# icon = PhotoImage(file="icon.png")
# icon = icon.subsample(35, 35)
# btn_delete = ttk.Button(window, image=icon)
btn_delete = ttk.Button(window, text = "DEL", command=btn_delete_clicked)
btn_delete.place(x=241,y = 0, width = 80, height=42)



if __name__ == "__main__":
    window.mainloop()



