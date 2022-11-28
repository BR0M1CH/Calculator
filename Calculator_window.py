from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re


import Calculator_functions as calc


def log_appender():
    global log
    log.append("warn2")

def get_exp():
    return(entr.get())


def ops_checker(expression):
    global log
    op_set = ("+-", "-+", "*/", "+/", "/+", "+*", "*+", "-/", "/-", "-*", "*-", "^-", "^+", "^*", "^/")
    for i in op_set:
        if i in expression:
            print("!!!Operator checker NOT DONE!!!")
            log.append("warn0")
            messagebox.showinfo("Ошибка", "Вы написали два операнда подряд")
            return(False)
    res = re.findall(r"([)][0-9]|[0-9][(])", expression)
    if len(res) != 0:
        print("!!!Operator Checker NOT DONE!!!")
        log.append("warn0")
        messagebox.showinfo("Ошибка","Вы пропустили знак между числом и скобкой")
        return(False)
    else: return(True)
        

def dot_checker_prev(expression):
    global log
    res = re.findall(r"[.]{2,}", expression)
    if len(res) != 0:
        print("!!!Prev Dot checker NOT DONE!!!")
        log.append("warn0")
        messagebox.showinfo("Ошибка", "В выражении присутствует несколько точек подряд")
        return(False)
    else: return(True)


def dot_checker(expression1):
    global log
    expression = [i for i in expression1]
    for i in expression:
        if expression == ".":
            print("!!!Dot checker NOT DONE!!!")
            log.append("warn1")
            messagebox.showinfo("Ошибка", "У вас в выражении одинокая точка...")
            return(False)
    return(True)


def bracket_checker(expression1):
    global log
    expression = ""
    for i in expression1: expression += "".join(i)
    if expression.count("(") != expression.count(")"):
        print("!!!Bracket checker NOT DONE!!!")
        log.append("warn1")
        messagebox.showinfo("Ошибка", "Количество открывающих скобок отлично от количества закрывающих скобок, устраните проблему")
        return(False)
    else: return(True)


def complex_checker(expression1):
    global log
    expression=[i for i in expression1]
    res = []
    for i in range(len(expression)):
        if "i" in expression[i]:
            res.append(i)
    for i in res:
        if expression[i].count("i") > 1:
            print("!!!Complex cheker NOT DONE!!!")
            log.append("warn1")
            messagebox.showinfo("Ошибка", "Вы ввели больше одного символа 'i' подряд")
            return(False)
    if "i" in expression[-1]:
        print("!!!Complex Checker NOT DONE!!!")
        log.append("warn1")
        messagebox.showinfo("Ошибка", f"Ошибка в заключении комплексного числа в скобки, проверьте {expression[i-2]}{expression[i-1]}{expression[i]}")
        return(False)
    for i in res:
        if (expression[i+1]!=")") or (expression[i-3] != "("):
            print("!!!Complex cheker NOT DONE!!!")
            log.append("warn1")
            messagebox.showinfo("Ошибка", f"Ошибка в заключении комплексного числа в скобки, проверьте {expression[i-2]}{expression[i-1]}{expression[i]}")
            return(False)
    return(True)


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
        expression = entr.get()
        print("CHECKERS0=", dot_checker_prev(expression), ops_checker(expression))
        if not ops_checker(expression):
            return
        elif not dot_checker_prev(expression):
            return
        else:
            expression = calc.enter_splitter(expression)
        print("CHEKERS1= ", dot_checker(expression), bracket_checker(expression),complex_checker(expression))
        if not bracket_checker(expression):
            return
        elif not complex_checker(expression): 
            return
        elif not dot_checker(expression):
            return
        else:
            print("Checker DONE")
            log.append("=")
        expression = calc.complex_converter(expression)
        print("Complex convertation DONE")
        while "(" in expression:
            left_index, right_index = calc.bracket_finder(expression)
            if calc.bracket_calc(left_index, right_index, expression) == "Error":
                return
            else:
                expression = calc.bracket_calc(left_index, right_index, expression)
        print("Bracket calculation DONE")
        while len(expression)>1:
            if calc.main_calc(expression) == "Error":
                return
            else:
                expression = calc.main_calc(expression)
        print("Main calculation DONE")
        expression = expression[0]
        if expression.imag == 0j:
            expression = round(expression.real,4)
        else:
            expression = complex(round(expression.real, 4), round(expression.imag,4))
        entr.insert(END, f"={expression}")
        log[-1] += "".join(str(expression))
    else:
        entr.delete(0, END)
        entr.insert(0, log[-1])
        entr.delete(0,1)
        log.append("last desicion returned")

    

def light_theme():
    btn_0.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_0.bind("<Enter>", lambda e:btn_0.configure(bg="#EEEED5"))
    btn_0.bind("<Leave>", lambda e:btn_0.configure(bg="#FFFFE4"))
    btn_1.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_1.bind("<Enter>", lambda e:btn_1.configure(bg="#EEEED5"))
    btn_1.bind("<Leave>", lambda e:btn_1.configure(bg="#FFFFE4"))
    btn_2.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_2.bind("<Enter>", lambda e:btn_2.configure(bg="#EEEED5"))
    btn_2.bind("<Leave>", lambda e:btn_2.configure(bg="#FFFFE4"))
    btn_3.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_3.bind("<Enter>", lambda e:btn_3.configure(bg="#EEEED5"))
    btn_3.bind("<Leave>", lambda e:btn_3.configure(bg="#FFFFE4"))
    btn_4.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_4.bind("<Enter>", lambda e:btn_4.configure(bg="#EEEED5"))
    btn_4.bind("<Leave>", lambda e:btn_4.configure(bg="#FFFFE4"))
    btn_5.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_5.bind("<Enter>", lambda e:btn_5.configure(bg="#EEEED5"))
    btn_5.bind("<Leave>", lambda e:btn_5.configure(bg="#FFFFE4"))
    btn_6.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_6.bind("<Enter>", lambda e:btn_6.configure(bg="#EEEED5"))
    btn_6.bind("<Leave>", lambda e:btn_6.configure(bg="#FFFFE4"))
    btn_7.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_7.bind("<Enter>", lambda e:btn_7.configure(bg="#EEEED5"))
    btn_7.bind("<Leave>", lambda e:btn_7.configure(bg="#FFFFE4"))
    btn_8.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_8.bind("<Enter>", lambda e:btn_8.configure(bg="#EEEED5"))
    btn_8.bind("<Leave>", lambda e:btn_8.configure(bg="#FFFFE4"))
    btn_9.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_9.bind("<Enter>", lambda e:btn_9.configure(bg="#EEEED5"))
    btn_9.bind("<Leave>", lambda e:btn_9.configure(bg="#FFFFE4"))
    btn_equal.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_equal.bind("<Enter>", lambda e:btn_equal.configure(bg="#EEEED5"))
    btn_equal.bind("<Leave>", lambda e:btn_equal.configure(bg="#FFFFE4"))
    btn_delete.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_delete.bind("<Enter>", lambda e:btn_delete.configure(bg="#EEEED5"))
    btn_delete.bind("<Leave>", lambda e:btn_delete.configure(bg="#FFFFE4"))
    btn_clear.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_clear.bind("<Enter>", lambda e:btn_clear.configure(bg="#EEEED5"))
    btn_clear.bind("<Leave>", lambda e:btn_clear.configure(bg="#FFFFE4"))
    btn_substraction.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_substraction.bind("<Enter>", lambda e:btn_substraction.configure(bg="#EEEED5"))
    btn_substraction.bind("<Leave>", lambda e:btn_substraction.configure(bg="#FFFFE4"))
    btn_multiplication.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_multiplication.bind("<Enter>", lambda e:btn_multiplication.configure(bg="#EEEED5"))
    btn_multiplication.bind("<Leave>", lambda e:btn_multiplication.configure(bg="#FFFFE4"))
    btn_division.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_division.bind("<Enter>", lambda e:btn_division.configure(bg="#EEEED5"))
    btn_division.bind("<Leave>", lambda e:btn_division.configure(bg="#FFFFE4"))
    btn_addition.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_addition.bind("<Enter>", lambda e:btn_addition.configure(bg="#EEEED5"))
    btn_addition.bind("<Leave>", lambda e:btn_addition.configure(bg="#FFFFE4"))
    btn_dot.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_dot.bind("<Enter>", lambda e:btn_dot.configure(bg="#EEEED5"))
    btn_dot.bind("<Leave>", lambda e:btn_dot.configure(bg="#FFFFE4"))
    btn_left_bracket.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_left_bracket.bind("<Enter>", lambda e:btn_left_bracket.configure(bg="#EEEED5"))
    btn_left_bracket.bind("<Leave>", lambda e:btn_left_bracket.configure(bg="#FFFFE4"))
    btn_right_bracket.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_right_bracket.bind("<Enter>", lambda e:btn_right_bracket.configure(bg="#EEEED5"))
    btn_right_bracket.bind("<Leave>", lambda e:btn_right_bracket.configure(bg="#FFFFE4"))
    btn_power.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_power.bind("<Enter>", lambda e:btn_power.configure(bg="#EEEED5"))
    btn_power.bind("<Leave>", lambda e:btn_power.configure(bg="#FFFFE4"))
    btn_clearlog.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_clearlog.bind("<Enter>", lambda e:btn_clearlog.configure(bg="#EEEED5"))
    btn_clearlog.bind("<Leave>", lambda e:btn_clearlog.configure(bg="#FFFFE4"))
    btn_i.configure(background="#FFFFE4", foreground="#848470", activebackground="#CDCDB7", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_i.bind("<Enter>", lambda e:btn_i.configure(bg="#EEEED5"))
    btn_i.bind("<Leave>", lambda e:btn_i.configure(bg="#FFFFE4"))
    entr.configure(background="#FFFFC0", fg="#303030", selectbackground="#CDCDB7" )
    entr.bind("<Enter>", lambda e:entr.configure(bg="#EEEED5"))
    entr.bind("<Leave>", lambda e:entr.configure(bg="#FFFFE4"))

def dark_theme():
    btn_0.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_0.bind("<Enter>", lambda e:btn_0.configure(bg="#666666"))
    btn_0.bind("<Leave>", lambda e:btn_0.configure(bg="#787878"))
    btn_1.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_1.bind("<Enter>", lambda e:btn_1.configure(bg="#666666"))
    btn_1.bind("<Leave>", lambda e:btn_1.configure(bg="#787878"))
    btn_2.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_2.bind("<Enter>", lambda e:btn_2.configure(bg="#666666"))
    btn_2.bind("<Leave>", lambda e:btn_2.configure(bg="#787878"))
    btn_3.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_3.bind("<Enter>", lambda e:btn_3.configure(bg="#666666"))
    btn_3.bind("<Leave>", lambda e:btn_3.configure(bg="#787878"))
    btn_4.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_4.bind("<Enter>", lambda e:btn_4.configure(bg="#666666"))
    btn_4.bind("<Leave>", lambda e:btn_4.configure(bg="#787878"))
    btn_5.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_5.bind("<Enter>", lambda e:btn_5.configure(bg="#666666"))
    btn_5.bind("<Leave>", lambda e:btn_5.configure(bg="#787878"))
    btn_6.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_6.bind("<Enter>", lambda e:btn_6.configure(bg="#666666"))
    btn_6.bind("<Leave>", lambda e:btn_6.configure(bg="#787878"))
    btn_7.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_7.bind("<Enter>", lambda e:btn_7.configure(bg="#666666"))
    btn_7.bind("<Leave>", lambda e:btn_7.configure(bg="#787878"))
    btn_8.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_8.bind("<Enter>", lambda e:btn_8.configure(bg="#666666"))
    btn_8.bind("<Leave>", lambda e:btn_8.configure(bg="#787878"))
    btn_9.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_9.bind("<Enter>", lambda e:btn_9.configure(bg="#666666"))
    btn_9.bind("<Leave>", lambda e:btn_9.configure(bg="#787878"))
    btn_equal.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_equal.bind("<Enter>", lambda e:btn_equal.configure(bg="#666666"))
    btn_equal.bind("<Leave>", lambda e:btn_equal.configure(bg="#787878"))
    btn_delete.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_delete.bind("<Enter>", lambda e:btn_delete.configure(bg="#666666"))
    btn_delete.bind("<Leave>", lambda e:btn_delete.configure(bg="#787878"))
    btn_clear.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_clear.bind("<Enter>", lambda e:btn_clear.configure(bg="#666666"))
    btn_clear.bind("<Leave>", lambda e:btn_clear.configure(bg="#787878"))
    btn_substraction.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_substraction.bind("<Enter>", lambda e:btn_substraction.configure(bg="#666666"))
    btn_substraction.bind("<Leave>", lambda e:btn_substraction.configure(bg="#787878"))
    btn_multiplication.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_multiplication.bind("<Enter>", lambda e:btn_multiplication.configure(bg="#666666"))
    btn_multiplication.bind("<Leave>", lambda e:btn_multiplication.configure(bg="#787878"))
    btn_division.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_division.bind("<Enter>", lambda e:btn_division.configure(bg="#666666"))
    btn_division.bind("<Leave>", lambda e:btn_division.configure(bg="#787878"))
    btn_addition.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_addition.bind("<Enter>", lambda e:btn_addition.configure(bg="#666666"))
    btn_addition.bind("<Leave>", lambda e:btn_addition.configure(bg="#787878"))
    btn_dot.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_dot.bind("<Enter>", lambda e:btn_dot.configure(bg="#666666"))
    btn_dot.bind("<Leave>", lambda e:btn_dot.configure(bg="#787878"))
    btn_left_bracket.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_left_bracket.bind("<Enter>", lambda e:btn_left_bracket.configure(bg="#666666"))
    btn_left_bracket.bind("<Leave>", lambda e:btn_left_bracket.configure(bg="#787878"))
    btn_right_bracket.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_right_bracket.bind("<Enter>", lambda e:btn_right_bracket.configure(bg="#666666"))
    btn_right_bracket.bind("<Leave>", lambda e:btn_right_bracket.configure(bg="#787878"))
    btn_power.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_power.bind("<Enter>", lambda e:btn_power.configure(bg="#666666"))
    btn_power.bind("<Leave>", lambda e:btn_power.configure(bg="#787878"))
    btn_clearlog.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_clearlog.bind("<Enter>", lambda e:btn_clearlog.configure(bg="#666666"))
    btn_clearlog.bind("<Leave>", lambda e:btn_clearlog.configure(bg="#787878"))
    btn_i.configure(background="#787878", foreground="#FFA500", activebackground="#404040", activeforeground="#FF8C00", font="Impact 12", relief=FLAT)
    btn_i.bind("<Enter>", lambda e:btn_i.configure(bg="#666666"))
    btn_i.bind("<Leave>", lambda e:btn_i.configure(bg="#787878"))
    entr.configure(background="#FFFFC0", fg="#303030", selectbackground="#CDCDB7" )
    entr.bind("<Enter>", lambda e:entr.configure(bg="#666666"))
    entr.bind("<Leave>", lambda e:entr.configure(bg="#787878"))


window = Tk()
window.title("Calculator")
window.geometry("325x445")


entr = Entry(window)
entr.place(x=1, y=1, width=239, height=40)
entr.bind("<Key>", lambda e: "break")

btn_1 = Button(window,text = "1", command=btn_1_clicked, )
btn_1.place(x=1, y= 121,width=80, height=80)

btn_2=Button(window, text = "2", command=btn_2_clicked)
btn_2.place(x=81, y= 121,width=80, height=80)

btn_3=Button(window, text = "3", command=btn_3_clicked)
btn_3.place(x=161, y= 121,width=80, height=80)

btn_4=Button(window, text = "4", command=btn_4_clicked)
btn_4.place(x=1, y= 201,width=80, height=80)

btn_5 = Button(window, text = "5", command=btn_5_clicked)
btn_5.place(x=81, y= 201,width=80, height=80)

btn_6=Button(window, text="6", command=btn_6_clicked)
btn_6.place(x=161, y= 201,width=80, height=80)

btn_7 = Button(window, text = "7", command=btn_7_clicked)
btn_7.place(x=1, y= 281,width=80, height=80)

btn_8 = Button(window, text = "8", command=btn_8_clicked)
btn_8.place(x=81, y=281,width=80, height=80)

btn_9 = Button(window, text = "9", command=btn_9_clicked)
btn_9.place(x=161, y= 281,width=80, height=80)

btn_clear = Button(window, text = "C", command=btn_clear_clicked)
btn_clear.place(x=241,y = 0, width = 40, height=20)

btn_left_bracket = Button(window, text = "(", command=btn_left_bracket_clicked)
btn_left_bracket.place(x=81,y = 41, width = 80, height=80)

btn_right_bracket = Button(window, text = ")", command=btn_right_bracket_clicked)
btn_right_bracket.place(x=161,y = 41, width = 80, height=80)

btn_multiplication = Button(window, text = "*", command=btn_multiplication_clicked)
btn_multiplication.place(x=241,y = 41, width = 80, height=80)

btn_division = Button(window, text = "/", command=btn_division_clicked)
btn_division.place(x=241,y = 121, width = 80, height=80)

btn_addition = Button(window, text = "+", command=btn_addition_clicked)
btn_addition.place(x=241,y = 201, width = 80, height=80)

btn_substraction = Button(window, text = "-", command=btn_substraction_clicked)
btn_substraction.place(x=241,y = 281, width = 80, height=80)

btn_dot = Button(window, text = ".", command=btn_dot_clicked)
btn_dot.place(x=1,y = 361, width = 80, height=80)

btn_0 = Button(window, text = "0", command=btn_0_clicked)
btn_0.place(x=81,y = 361, width = 80, height=80)

btn_power = Button(window, text = "^", command=btn_power_clicked)
btn_power.place(x=161,y = 361, width = 80, height=80)

btn_equal = Button(window, text = "=", command=btn_equal_clicked)
btn_equal.place(x=241,y = 361, width = 80, height=80)

btn_delete = Button(window, text = "DEL", command=btn_delete_clicked)
btn_delete.place(x=241,y = 20, width = 80, height=21)

btn_clearlog = Button(window, text = "CL", command = btn_clearlog_clicked)
btn_clearlog.place(x=281, y=0, width=40, height=20)

btn_i= Button(window, text = "i", command = btn_i_clicked)
btn_i.place(x=1, y=41, width=80, height=80)

dark_theme()

log = []

if __name__ == "__main__":
    window.mainloop()
