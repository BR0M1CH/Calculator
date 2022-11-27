import re
from TEST import get_exp, bracket_checker
from tkinter import *
from tkinter import ttk

def enter_splitter(expression):
    expression = re.split(r"([0-9.ij]+)|(\W^.)?", expression)
    while "" in expression: expression.remove("")
    while None in expression: expression.remove(None)
    return(expression)


def bracket_finder(expression1):
    expression = [i for i in expression1]
    print(expression)
    nums = expression.count("(")
    nums1 = nums
    left_bracket = 0
    for i in range(nums):
        print(expression)
        if expression[0]=="(" and nums1 == 1:
            left_bracket = int(0)
        else:
            left_bracket = expression.index("(", left_bracket+1)
            nums1-=1
    right_bracket = expression.index(")", left_bracket)
    return left_bracket, right_bracket


def calc_func(op, index, iterable1):
    iterable = [i for i in iterable1]
    iterable[index-1] = complex(iterable[index-1])
    iterable[index+1] = complex(iterable[index+1])
    if op == "*":
        iterable[index] = (iterable[index-1]) * (iterable[index+1])
        iterable.pop(index+1)
        iterable.pop(index-1)
    elif op == "/":
        iterable[index] = (iterable[index-1]) / (iterable[index+1])
        iterable.pop(index+1)
        iterable.pop(index-1)
    elif op == "+":
        iterable[index] = (iterable[index-1]) + (iterable[index+1])
        iterable.pop(index+1)
        iterable.pop(index-1)
    elif op == "-":
        iterable[index] = (iterable[index-1]) - (iterable[index+1])
        iterable.pop(index+1)
        iterable.pop(index-1)
    elif op == "^":
        iterable[index] = pow(iterable[index-1], iterable[index+1])
        iterable.pop(index+1)
        iterable.pop(index-1)
    return(iterable)
            

def bracket_calc(left_index, right_index, expression1):
    helper= []
    expression = [i for i in expression1]
    if (right_index - left_index) > 2:
        for i in range(left_index+1, right_index):
            helper.append(expression[i])
        helper_index = index_in_dict_pow("^", helper)
        while helper_index != []:
            helper = calc_func(helper[helper_index[0]],helper_index[0],helper)
            helper_index.pop(0)
        helper_index = index_in_dict("*", "/", helper)
        while helper_index != []:
            helper = calc_func(helper[helper_index[0]],helper_index[0],helper)
            helper_index.pop(0)
        helper_index = index_in_dict("+", "-", helper)
        while helper_index != []:
            helper = calc_func(helper[helper_index[0]],helper_index[0],helper)
            helper_index.pop(0)
        for i in range(right_index, left_index, -1):
            expression.pop(i)
        expression[left_index] = helper[0]
        helper.clear()
    else:
        expression.pop(right_index)
        expression.pop(left_index)
    return expression

def main_calc(expression1):
    expression = [i for i in expression1]
    while "^" in expression:
        helper_index = index_in_dict_pow("^", expression)
        expression = calc_func(expression[helper_index[0]], helper_index[0], expression)
        helper_index.pop(0)
    while "*" in expression or "/" in expression:
        helper_index = index_in_dict("*", "/", expression)
        expression = calc_func(expression[helper_index[0]], helper_index[0], expression)
        helper_index.pop(0)
    while "+" in expression or "-" in expression:
        helper_index = index_in_dict("+", "-", expression)
        expression = calc_func(expression[helper_index[0]], helper_index[0], expression)
        helper_index.pop(0)
    return(expression)




def index_in_dict(op1, op2, iterable):                #Возвращает список индексов двух указанных операторов в указываемом списке
    helper_index = []
    for i in range(len(iterable)):
        if iterable[i] == op1 or iterable[i] == op2:
            helper_index.append(i)
    return helper_index

def index_in_dict_pow(op1, iterable):                #Возвращает список индексов двух указанных операторов в указываемом списке
    helper_index = []
    for i in range(len(iterable)):
        if iterable[i] == op1:
            helper_index.append(i)
    return helper_index


def complex_converter(expression1):
    expression = [i for i in expression1]
    for i in range(len(expression)):
        if "i" in expression[i] or "j" in expression[i]:
            if "i" in expression[i]:
                expression[i] = re.sub('i', 'j', expression[i]) 
            for j in range(i-1, i+1):
                expression[i-2]+="".join(expression[j])
            for j in range(i-1, i+1):
                expression[j] = None
    while None in expression:
        expression.remove(None)
    return(expression)