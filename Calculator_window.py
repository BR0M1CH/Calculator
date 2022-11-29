from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import time
import json


import Calculator_functions as calc


def log_to_json():
    global log
    with open("LOGS.json", "r") as l:
        log_1 = json.load(l)
    log.update(log_1)
    with open("LOGS.json", "w") as l:
        json.dump(log, l, indent=4)


def full_log_clear():
    global log
    with open("LOGS.json", "w") as l:
        json.dump("", l)

def log_show():
    global log
    messagebox.showinfo("Logs", log)


def log_appender():
    global log
    log[time.time()]=("warn2")

def get_exp():
    return(entr.get())


def ops_checker(expression):
    global log
    op_set = ("+-", "-+", "*/", "+/", "/+", "+*", "*+", "-/", "/-", "-*", "*-", "^-", "^+", "^*", "^/", "+)", "*)", "-)", "/)", "^)","(+","(-","(*","(/","(^", "(.", ").")
    for i in op_set:
        if i in expression:
            print("!!!Operator checker NOT DONE!!!")
            log[time.time()]=("warn0")
            messagebox.showwarning("Ошибка", "Вы написали два операнда подряд")
            return(False)
    res = re.findall(r"([)][0-9]|[0-9][(])", expression)
    if len(res) != 0:
        print("!!!Operator Checker NOT DONE!!!")
        log[time.time()]=("warn0")
        messagebox.showwarning("Ошибка","Вы пропустили знак между числом и скобкой")
        return(False)
    return(True)
        

def dot_checker_prev(expression):
    global log
    res = re.findall(r"[.]{2,}", expression)
    if len(res) != 0:
        print("!!!Prev Dot checker NOT DONE!!!")
        log[time.time()]=("warn0")
        messagebox.showwarning("Ошибка", "В выражении присутствует несколько точек подряд")
        return(False)
    return(True)


def dot_checker(expression1):
    global log
    expression = [i for i in expression1]
    for i in expression:
        if i == ".":
            print("!!!Dot checker NOT DONE!!!")
            log[time.time()]=("warn1")
            messagebox.showwarning("Ошибка", "У вас в выражении одинокая точка...")
            return(False)
    return(True)


def bracket_checker(expression1):
    global log
    expression = ""
    for i in expression1: expression += "".join(i)
    if expression.count("(") != expression.count(")"):
        print("!!!Bracket checker NOT DONE!!!")
        log[time.time()]=("warn1")
        messagebox.showwarning("Ошибка", "Количество открывающих скобок отлично от количества закрывающих скобок, устраните проблему")
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
            log[time.time()]=("warn1")
            messagebox.showwarning("Ошибка", "Вы ввели больше одного символа 'i' подряд")
            return(False)
    if "i" in expression[-1]:
        print("!!!Complex Checker NOT DONE!!!")
        log[time.time()]=("warn1")
        messagebox.showwarning("Ошибка", f"Ошибка в заключении комплексного числа в скобки, проверьте {expression[i-2]}{expression[i-1]}{expression[i]}")
        return(False)
    for i in res:
        if (expression[i+1]!=")") or (expression[i-3] != "("):
            print("!!!Complex cheker NOT DONE!!!")
            log[time.time()]=("warn1")
            messagebox.showwarning("Ошибка", f"Ошибка в заключении комплексного числа в скобки, проверьте {expression[i-2]}{expression[i-1]}{expression[i]}")
            return(False)
    return(True)


def get_index():
    return(entr.index(INSERT))

def btn_1_clicked():
    global log
    entr.insert(get_index(), "1")
    log[time.time()] = "1"

def btn_2_clicked():
    global log
    entr.insert(get_index(), "2")
    log[time.time()] = "2"

def btn_3_clicked():
    global log
    entr.insert(get_index(), "3")
    log[time.time()] = "3"

def btn_4_clicked():
    global log
    entr.insert(get_index(), "4")
    log[time.time()] = "4"

def btn_5_clicked():
    global log
    entr.insert(get_index(), "5")
    log[time.time()] = "5"

def btn_6_clicked():
    global log
    entr.insert(get_index(), "6")
    log[time.time()] = "6"

def btn_7_clicked():
    global log
    entr.insert(get_index(), "7")
    log[time.time()] = "7"

def btn_8_clicked():
    global log
    entr.insert(get_index(), "8")
    log[time.time()] = "8"

def btn_9_clicked():
    global log
    entr.insert(get_index(), "9")
    log[time.time()] = "9"

def btn_0_clicked():
    global log
    entr.insert(get_index(), "0")
    log[time.time()] = "0"

def btn_multiplication_clicked():
    global log
    entr.insert(get_index(), "*")
    log[time.time()] = "*"

def btn_addition_clicked():
    global log
    entr.insert(get_index(), "+")
    log[time.time()] = "+"

def btn_division_clicked():
    global log
    entr.insert(get_index(), "/")
    log[time.time()] = "/"

def btn_substraction_clicked():
    global log
    entr.insert(get_index(), "-")
    log[time.time()] = "-"

def btn_power_clicked():
    global log
    entr.insert(get_index(), "^")
    log[time.time()] = "^"

def btn_right_bracket_clicked():
    global log
    entr.insert(get_index(), ")")
    log[time.time()] = ")"

def btn_clearlog_clicked():
    global log
    log.clear()

def btn_left_bracket_clicked():
    global log
    entr.insert(get_index(), "(")
    log[time.time()] = "("

def btn_delete_clicked():
    global log
    entr.delete(first=get_index()-1, last=None)
    log[time.time()] = "DEL"

def btn_clear_clicked():
    global log
    entr.delete(first=0, last = END)
    log[time.time()] = "CLEAR"

def btn_dot_clicked():
    global log
    entr.insert(get_index(), ".")
    log[time.time()] = "."

def btn_i_clicked():
    global log
    entr.insert(get_index(), "i")
    log[time.time()] = "i"

def btn_equal_clicked():
    global log
    if "=" not in log[next(reversed(log.keys()))]:
        expression = entr.get()
        if not ops_checker(expression):
            return
        elif not dot_checker_prev(expression):
            return
        else:
            expression = calc.enter_splitter(expression)
        if not bracket_checker(expression):
            return
        elif not complex_checker(expression): 
            return
        elif not dot_checker(expression):
            return
        else:
            print("Checker DONE")
            log[time.time()] = "="
        expression = calc.complex_converter(expression)
        print("Complex convertation DONE")
        while "(" in expression:
            left_index, right_index = calc.bracket_finder(expression)
            if calc.bracket_calc(left_index, right_index, expression) == "Error":
                log[time.asctime()] = "warn2"
                return
            else:
                expression = calc.bracket_calc(left_index, right_index, expression)
        print("Bracket calculation DONE")
        while len(expression)>1:
            if calc.main_calc(expression) == "Error":
                log[time.asctime()] = "warn2"
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
        log[next(reversed(log.keys()))] += "".join(str(expression))
    else:
        entr.delete(0, END)
        entr.insert(0, log[next(reversed(log.keys()))])
        entr.delete(0,1)
        log[time.time()]=("last desicion returned")

    
background="#6B6B6B"
def light_theme():
    btn_0.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_0.bind("<Enter>", lambda e:btn_0.configure(bg="#A2B5CD"))
    btn_0.bind("<Leave>", lambda e:btn_0.configure(bg="#CAE1FF"))
    btn_1.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_1.bind("<Enter>", lambda e:btn_1.configure(bg="#A2B5CD"))
    btn_1.bind("<Leave>", lambda e:btn_1.configure(bg="#CAE1FF"))
    btn_2.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_2.bind("<Enter>", lambda e:btn_2.configure(bg="#A2B5CD"))
    btn_2.bind("<Leave>", lambda e:btn_2.configure(bg="#CAE1FF"))
    btn_3.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_3.bind("<Enter>", lambda e:btn_3.configure(bg="#A2B5CD"))
    btn_3.bind("<Leave>", lambda e:btn_3.configure(bg="#CAE1FF"))
    btn_4.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_4.bind("<Enter>", lambda e:btn_4.configure(bg="#A2B5CD"))
    btn_4.bind("<Leave>", lambda e:btn_4.configure(bg="#CAE1FF"))
    btn_5.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_5.bind("<Enter>", lambda e:btn_5.configure(bg="#A2B5CD"))
    btn_5.bind("<Leave>", lambda e:btn_5.configure(bg="#CAE1FF"))
    btn_6.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_6.bind("<Enter>", lambda e:btn_6.configure(bg="#A2B5CD"))
    btn_6.bind("<Leave>", lambda e:btn_6.configure(bg="#CAE1FF"))
    btn_7.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_7.bind("<Enter>", lambda e:btn_7.configure(bg="#A2B5CD"))
    btn_7.bind("<Leave>", lambda e:btn_7.configure(bg="#CAE1FF"))
    btn_8.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_8.bind("<Enter>", lambda e:btn_8.configure(bg="#A2B5CD"))
    btn_8.bind("<Leave>", lambda e:btn_8.configure(bg="#CAE1FF"))
    btn_9.configure(background="#CAE1FF", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_9.bind("<Enter>", lambda e:btn_9.configure(bg="#A2B5CD"))
    btn_9.bind("<Leave>", lambda e:btn_9.configure(bg="#CAE1FF"))
    btn_equal.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_equal.bind("<Enter>", lambda e:btn_equal.configure(bg="#A2B5CD"))
    btn_equal.bind("<Leave>", lambda e:btn_equal.configure(bg="#A2B5CD"))
    btn_delete.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_delete.bind("<Enter>", lambda e:btn_delete.configure(bg="#A2B5CD"))
    btn_delete.bind("<Leave>", lambda e:btn_delete.configure(bg="#BCD2EE"))
    btn_clear.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A", font="Impact 12", relief=FLAT)
    btn_clear.bind("<Enter>", lambda e:btn_clear.configure(bg="#A2B5CD"))
    btn_clear.bind("<Leave>", lambda e:btn_clear.configure(bg="#BCD2EE"))
    btn_substraction.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_substraction.bind("<Enter>", lambda e:btn_substraction.configure(bg="#A2B5CD"))
    btn_substraction.bind("<Leave>", lambda e:btn_substraction.configure(bg="#BCD2EE"))
    btn_multiplication.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_multiplication.bind("<Enter>", lambda e:btn_multiplication.configure(bg="#A2B5CD"))
    btn_multiplication.bind("<Leave>", lambda e:btn_multiplication.configure(bg="#BCD2EE"))
    btn_division.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_division.bind("<Enter>", lambda e:btn_division.configure(bg="#A2B5CD"))
    btn_division.bind("<Leave>", lambda e:btn_division.configure(bg="#BCD2EE"))
    btn_addition.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_addition.bind("<Enter>", lambda e:btn_addition.configure(bg="#A2B5CD"))
    btn_addition.bind("<Leave>", lambda e:btn_addition.configure(bg="#BCD2EE"))
    btn_dot.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_dot.bind("<Enter>", lambda e:btn_dot.configure(bg="#A2B5CD"))
    btn_dot.bind("<Leave>", lambda e:btn_dot.configure(bg="#BCD2EE"))
    btn_left_bracket.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_left_bracket.bind("<Enter>", lambda e:btn_left_bracket.configure(bg="#A2B5CD"))
    btn_left_bracket.bind("<Leave>", lambda e:btn_left_bracket.configure(bg="#BCD2EE"))
    btn_right_bracket.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_right_bracket.bind("<Enter>", lambda e:btn_right_bracket.configure(bg="#A2B5CD"))
    btn_right_bracket.bind("<Leave>", lambda e:btn_right_bracket.configure(bg="#BCD2EE"))
    btn_power.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_power.bind("<Enter>", lambda e:btn_power.configure(bg="#A2B5CD"))
    btn_power.bind("<Leave>", lambda e:btn_power.configure(bg="#BCD2EE"))
    btn_clearlog.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_clearlog.bind("<Enter>", lambda e:btn_clearlog.configure(bg="#A2B5CD"))
    btn_clearlog.bind("<Leave>", lambda e:btn_clearlog.configure(bg="#BCD2EE"))
    btn_i.configure(background="#BCD2EE", foreground="#6B6B6B", activebackground="#6E7B8B", activeforeground="#6A6A5A",  font="Impact 12", relief=FLAT)
    btn_i.bind("<Enter>", lambda e:btn_i.configure(bg="#A2B5CD"))
    btn_i.bind("<Leave>", lambda e:btn_i.configure(bg="#BCD2EE"))
    window.configure(background="white")
    entr.configure(background="white", fg="#303030", selectbackground="#CDCDB7", font="Dubai", insertbackground="#6B6B6B" )
    menu.configure(background="#CAE1FF", foreground="#6A6A5A", activebackground="#A2B5CD", activeforeground="#6A6A5A")
    log[time.time()] = "Light Theme"


def dark_theme():
    bg_main ="#383838"
    bg_per = "#2B2B2B"
    act_bg = "#4F4F4F"
    fg_main = "#FF8000"
    fg_per = "#FF6103"
    act_fg = "#C76114"
    bg_ent = "#474747"
    btn_0.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_0.bind("<Enter>", lambda e:btn_0.configure(bg=bg_ent))
    btn_0.bind("<Leave>", lambda e:btn_0.configure(bg=bg_main))
    btn_1.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_1.bind("<Enter>", lambda e:btn_1.configure(bg=bg_ent))
    btn_1.bind("<Leave>", lambda e:btn_1.configure(bg=bg_main))
    btn_2.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_2.bind("<Enter>", lambda e:btn_2.configure(bg=bg_ent))
    btn_2.bind("<Leave>", lambda e:btn_2.configure(bg=bg_main))
    btn_3.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_3.bind("<Enter>", lambda e:btn_3.configure(bg=bg_ent))
    btn_3.bind("<Leave>", lambda e:btn_3.configure(bg=bg_main))
    btn_4.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_4.bind("<Enter>", lambda e:btn_4.configure(bg=bg_ent))
    btn_4.bind("<Leave>", lambda e:btn_4.configure(bg=bg_main))
    btn_5.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_5.bind("<Enter>", lambda e:btn_5.configure(bg=bg_ent))
    btn_5.bind("<Leave>", lambda e:btn_5.configure(bg=bg_main))
    btn_6.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_6.bind("<Enter>", lambda e:btn_6.configure(bg=bg_ent))
    btn_6.bind("<Leave>", lambda e:btn_6.configure(bg=bg_main))
    btn_7.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_7.bind("<Enter>", lambda e:btn_7.configure(bg=bg_ent))
    btn_7.bind("<Leave>", lambda e:btn_7.configure(bg=bg_main))
    btn_8.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_8.bind("<Enter>", lambda e:btn_8.configure(bg=bg_ent))
    btn_8.bind("<Leave>", lambda e:btn_8.configure(bg=bg_main))
    btn_9.configure(background=bg_main, foreground=fg_main, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_9.bind("<Enter>", lambda e:btn_9.configure(bg=bg_ent))
    btn_9.bind("<Leave>", lambda e:btn_9.configure(bg=bg_main))
    btn_equal.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_equal.bind("<Enter>", lambda e:btn_equal.configure(bg=bg_ent))
    btn_equal.bind("<Leave>", lambda e:btn_equal.configure(bg=bg_per))
    btn_delete.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_delete.bind("<Enter>", lambda e:btn_delete.configure(bg=bg_ent))
    btn_delete.bind("<Leave>", lambda e:btn_delete.configure(bg=bg_per))
    btn_clear.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_clear.bind("<Enter>", lambda e:btn_clear.configure(bg=bg_ent))
    btn_clear.bind("<Leave>", lambda e:btn_clear.configure(bg=bg_per))
    btn_substraction.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_substraction.bind("<Enter>", lambda e:btn_substraction.configure(bg=bg_ent))
    btn_substraction.bind("<Leave>", lambda e:btn_substraction.configure(bg=bg_per))
    btn_multiplication.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_multiplication.bind("<Enter>", lambda e:btn_multiplication.configure(bg=act_bg))
    btn_multiplication.bind("<Leave>", lambda e:btn_multiplication.configure(bg=bg_per))
    btn_division.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_division.bind("<Enter>", lambda e:btn_division.configure(bg=bg_ent))
    btn_division.bind("<Leave>", lambda e:btn_division.configure(bg=bg_per))
    btn_addition.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_addition.bind("<Enter>", lambda e:btn_addition.configure(bg=bg_ent))
    btn_addition.bind("<Leave>", lambda e:btn_addition.configure(bg=bg_per))
    btn_dot.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_dot.bind("<Enter>", lambda e:btn_dot.configure(bg=bg_ent))
    btn_dot.bind("<Leave>", lambda e:btn_dot.configure(bg=bg_per))
    btn_left_bracket.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_left_bracket.bind("<Enter>", lambda e:btn_left_bracket.configure(bg=bg_ent))
    btn_left_bracket.bind("<Leave>", lambda e:btn_left_bracket.configure(bg=bg_per))
    btn_right_bracket.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_right_bracket.bind("<Enter>", lambda e:btn_right_bracket.configure(bg=bg_ent))
    btn_right_bracket.bind("<Leave>", lambda e:btn_right_bracket.configure(bg=bg_per))
    btn_power.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_power.bind("<Enter>", lambda e:btn_power.configure(bg=bg_ent))
    btn_power.bind("<Leave>", lambda e:btn_power.configure(bg=bg_per))
    btn_clearlog.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_clearlog.bind("<Enter>", lambda e:btn_clearlog.configure(bg=bg_ent))
    btn_clearlog.bind("<Leave>", lambda e:btn_clearlog.configure(bg=bg_per))
    btn_i.configure(background=bg_per, foreground=fg_per, activebackground=act_bg, activeforeground=act_fg, font="Impact 12", relief=FLAT)
    btn_i.bind("<Enter>", lambda e:btn_i.configure(bg=bg_ent))
    btn_i.bind("<Leave>", lambda e:btn_i.configure(bg=bg_per))
    entr.configure(background=bg_main, fg=fg_main, selectbackground="#CDCDB7", font="Dubai", insertbackground=fg_per)
    window.configure(background="black")
    log[time.time()] = "Dark Theme"

if __name__ == "__main__":

    window = Tk()
    window.title("Calculator")
    window.geometry("325x447")
    window.resizable(False, False)


    entr = Entry(window, highlightthickness=0, insertborderwidth=0, relief=FLAT)
    entr.place(x=1, y=1, width=242, height=40)
    entr.bind("<Key>", lambda e: "break")

    btn_1 = Button(window,text = "1", command=btn_1_clicked, )
    btn_1.place(x=1, y= 123,width=80, height=80)

    btn_2=Button(window, text = "2", command=btn_2_clicked)
    btn_2.place(x=82, y= 123,width=80, height=80)

    btn_3=Button(window, text = "3", command=btn_3_clicked)
    btn_3.place(x=163, y= 123,width=80, height=80)

    btn_4=Button(window, text = "4", command=btn_4_clicked)
    btn_4.place(x=1, y= 204,width=80, height=80)

    btn_5 = Button(window, text = "5", command=btn_5_clicked)
    btn_5.place(x=82, y= 204,width=80, height=80)

    btn_6=Button(window, text="6", command=btn_6_clicked)
    btn_6.place(x=163, y= 204,width=80, height=80)

    btn_7 = Button(window, text = "7", command=btn_7_clicked)
    btn_7.place(x=1, y= 285,width=80, height=80)

    btn_8 = Button(window, text = "8", command=btn_8_clicked)
    btn_8.place(x=82, y=285,width=80, height=80)

    btn_9 = Button(window, text = "9", command=btn_9_clicked)
    btn_9.place(x=163, y= 285,width=80, height=80)

    btn_clear = Button(window, text = "C", command=btn_clear_clicked)
    btn_clear.place(x=244,y = 1, width = 40, height=19)

    btn_left_bracket = Button(window, text = "(", command=btn_left_bracket_clicked)
    btn_left_bracket.place(x=82,y = 42, width = 80, height=80)

    btn_right_bracket = Button(window, text = ")", command=btn_right_bracket_clicked)
    btn_right_bracket.place(x=163,y = 42, width = 80, height=80)

    btn_multiplication = Button(window, text = "*", command=btn_multiplication_clicked)
    btn_multiplication.place(x=244,y = 42, width = 80, height=80)

    btn_division = Button(window, text = "/", command=btn_division_clicked)
    btn_division.place(x=244,y = 123, width = 80, height=80)

    btn_addition = Button(window, text = "+", command=btn_addition_clicked)
    btn_addition.place(x=244,y = 204, width = 80, height=80)

    btn_substraction = Button(window, text = "-", command=btn_substraction_clicked)
    btn_substraction.place(x=244,y = 285, width = 80, height=80)

    btn_dot = Button(window, text = ".", command=btn_dot_clicked)
    btn_dot.place(x=1,y = 366, width = 80, height=80)

    btn_0 = Button(window, text = "0", command=btn_0_clicked)
    btn_0.place(x=82,y = 366, width = 80, height=80)

    btn_power = Button(window, text = "^", command=btn_power_clicked)
    btn_power.place(x=163,y = 366, width = 80, height=80)

    btn_equal = Button(window, text = "=", command=btn_equal_clicked)
    btn_equal.place(x=244,y = 366, width = 80, height=80)

    btn_delete = Button(window, text = "DEL", command=btn_delete_clicked)
    btn_delete.place(x=244,y = 21, width = 80, height=20)

    btn_clearlog = Button(window, text = "CL", command = btn_clearlog_clicked)
    btn_clearlog.place(x=285, y=1, width=39, height=19)

    btn_i= Button(window, text = "i", command = btn_i_clicked)
    btn_i.place(x=1, y=42, width=80, height=80)


    menu = Menu(window)
    theme = Menu(menu, tearoff=0)
    theme.add_command(label = "Light Theme", command=light_theme)
    theme.add_separator()
    theme.add_command(label = "Dark Theme", command = dark_theme)
    menu.add_cascade(label = "Theme", menu=theme)
    window.config(menu=menu)
    logs = Menu(menu, tearoff=0)
    logs.add_command(label="Export logs", command=log_to_json)
    logs.add_command(label = "Clear external log storage", command = full_log_clear)
    logs.add_command(label = "Show logs", command=log_show)
    menu.add_cascade(label = "Logs", menu=logs)
    log = {}

    dark_theme()



    window.mainloop()
