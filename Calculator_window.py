from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re



import Calculator_functions as calc


def get_exp():
    return(entr.get())

def wrong_enter(expression1):
    expression = ""
    for i in expression1: expression += "".join(i)
    a = 0
    result=re.findall(r"[^0-9ij*+-=/^().]", expression)
    if result != []:
        messagebox.showinfo("Ошибка", "Вы ввели некорректный символ")
        a = 1
    if expression.count("(") != expression.count(")"):
        messagebox.showinfo("Ошибка", "Количество открывающих скобок отлично от количества закрывающих скобок, устраните проблему")
        a = 1
    return(a)


def complex_checker(expression):
    print(expression)
    res, a = [], 0
    for i in range(len(expression)):
        if "i" in expression[i]:
            res.append(i)
    print(res)
    if "i" in expression[-1]:
            a = 1
            messagebox.showinfo("Ошибка", f"Ошибка в заключении комплексного числа в скобки, проверьте {expression[i-2]}{expression[i-1]}{expression[i]}")
    print(a)
    if a != 1:
        for i in res:
            if (expression[i+1]!=")") or (expression[i-3] != ")"):
                a = 1
                messagebox.showinfo("Ошибка", f"Ошибка в заключении комплексного числа в скобки, проверьте {expression[i-2]}{expression[i-1]}{expression[i]}")
                break
        return(a)


def get_index():
    return(entr.index(INSERT))

def btn_1_clicked():
    global log
    entr.insert(get_index(), "1")
    log.append("1")

def btn_2_clicked():
    global log
    entr.insert(get_index(), "2")
    log.append("2")

def btn_3_clicked():
    global log
    log.append("3")
    entr.insert(get_index(), "3")

def btn_4_clicked():
    global log
    log.append("4")
    entr.insert(get_index(), "4")

def btn_5_clicked():
    global log
    log.append("5")
    entr.insert(get_index(), "5")

def btn_6_clicked():
    global log
    log.append("6")
    entr.insert(get_index(), "6")

def btn_7_clicked():
    global log
    log.append("7")
    entr.insert(get_index(), "7")

def btn_8_clicked():
    global log
    log.append("8")
    entr.insert(get_index(), "8")

def btn_9_clicked():
    global log
    log.append("9")
    entr.insert(get_index(), "9")

def btn_0_clicked():
    global log
    log.append("0")
    entr.insert(get_index(), "0")

def btn_multiplication_clicked():
    global log
    log.append("*")
    entr.insert(get_index(), "*")

def btn_addition_clicked():
    global log
    log.append("+")
    entr.insert(get_index(), "+")

def btn_division_clicked():
    global log
    log.append("/")
    entr.insert(get_index(), "/")

def btn_substraction_clicked():
    global log
    log.append("-")
    entr.insert(get_index(), "-")

def btn_power_clicked():
    global log
    log.append("^")
    entr.insert(get_index(), "^")

def btn_right_bracket_clicked():
    global log
    log.append(")")
    entr.insert(get_index(), ")")

def btn_clearlog_clicked():
    global log
    log.clear()

def btn_left_bracket_clicked():
    global log
    log.append("(")
    entr.insert(get_index(), "(")

def btn_delete_clicked():
    global log
    log.append("DEL")
    entr.delete(first=get_index()-1, last=None)

def btn_clear_clicked():
    global log
    log.append("CLEAR")
    # txt.set("")
    entr.delete(first=0, last = END)

def btn_dot_clicked():
    global log
    log.append(".")
    entr.insert(get_index(), ".")

def btn_i_clicked():
    global log
    log.append("i")
    entr.insert(get_index(), "i")

def btn_equal_clicked():
    global log
    if "=" not in log[-1]:
        while True:
            try:
                expression = entr.get()
                expression = calc.enter_splitter(expression)
                print("Enter DONE")
                if wrong_enter(expression) == 1:
                    print("!!!Checker NOT DONE!!!")
                    raise Exception
                elif complex_checker(expression) == 1:
                    print("!!!Complex Cheker NOT DONE!!!")
                    raise Exception
                else:
                    print("Checker DONE")
                    log.append("=")
                    break
            except: btn_equal_clicked()
        expression = calc.complex_converter(expression)
        print("Complex convertation DONE")
        while "(" in expression:
            left_index, right_index = calc.bracket_finder(expression)
            expression = calc.bracket_calc(left_index, right_index, expression)
        print("Bracket calculation DONE")
        while len(expression)>1:
            expression = calc.main_calc(expression)
        print("Main calculation DONE")
        expression = expression[0]
        if expression.imag == 0j:
            expression = expression.real
        entr.insert(END, f"={expression}")
        log[-1] += "".join(str(expression))
    else:
        entr.delete(0, END)
        entr.insert(0, log[-1])
        entr.delete(0,1)




window = Tk()
window.title("Calculator")
window.geometry("325x445")

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
btn_clear.place(x=241,y = 0, width = 40, height=20)

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

btn_delete = ttk.Button(window, text = "DEL", command=btn_delete_clicked)
btn_delete.place(x=241,y = 20, width = 80, height=21)

btn_clearlog = ttk.Button(window, text = "CL", command = btn_clearlog_clicked)
btn_clearlog.place(x=281, y=0, width=40, height=20)

btn_i=ttk.Button(window, text = "i", command = btn_i_clicked)
btn_i.place(x=1, y=41, width=80, height=80)


warn = ttk.Label(window)

log = []

if __name__ == "__main__":
    window.mainloop()



