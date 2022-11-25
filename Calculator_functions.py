import re

helper = []

def enter():
    expression = str(input("Введите выражение: "))
    expression = re.split(r"([0-9]i)+|(\W)?", expression)
    while "" in expression: expression.remove("")
    while None in expression: expression.remove(None)
    return(expression)


def bracket_finder():
    global expression
    nums = expression.count("(")
    left_bracket = 0
    for i in range(nums):
        left_bracket = expression.index("(", left_bracket+1)
    right_bracket = expression.index(")", left_bracket)
    return left_bracket, right_bracket


def calc_func(op, index, iterable):
    global expression, helper
    if iterable is expression:
        expression[index-1] = complex(expression[index-1])
        expression[index+1] = complex(expression[index+1])
        if op == "*":
            expression[index] = (expression[index-1]) * (expression[index+1])
            expression.pop(index+1)
            expression.pop(index-1)
        elif op == "/":
            expression[index] = (expression[index-1]) / (expression[index+1])
            expression.pop(index+1)
            expression.pop(index-1)
        elif op == "+":
            expression[index] = (expression[index-1]) + (expression[index+1])
            expression.pop(index+1)
            expression.pop(index-1)
        elif op == "-":
            expression[index] = (expression[index-1]) - (expression[index+1])
            expression.pop(index+1)
            expression.pop(index-1)
    elif iterable is helper:
        helper[index-1] = complex(helper[index-1])
        helper[index+1] = complex(helper[index+1])
        if op == "*":
            helper[index] = (helper[index-1]) * (helper[index+1])
            helper.pop(index+1)
            helper.pop(index-1)
        elif op == "/":
            helper[index] = round((helper[index-1]) / (helper[index+1]), 5)
            helper.pop(index+1)
            helper.pop(index-1)
        elif op == "+":
            helper[index] = (helper[index-1]) + (helper[index+1])
            helper.pop(index+1)
            helper.pop(index-1)
        elif op == "-":
            helper[index] = (helper[index-1]) - (helper[index+1])
            helper.pop(index+1)
            helper.pop(index-1)
            

def bracket_calc(left_index, right_index):
    global expression, helper
    if (right_index - left_index) > 2:
        for i in range(left_index+1, right_index):
            helper.append(expression[i])
        helper_index = index_in_dict("*", "/", helper)
        while helper_index != []:
            calc_func(helper[helper_index[0]],helper_index[0],helper)
            helper_index.pop(0)
        helper_index = index_in_dict("+", "-", helper)
        while helper_index != []:
            calc_func(helper[helper_index[0]],helper_index[0],helper)
            helper_index.pop(0)
        for i in range(right_index, left_index, -1):
            expression.pop(i)
        expression[left_index] = helper[0]
        helper.clear()
    else:
        expression.pop(right_index)
        expression.pop(left_index)


def main_calc():
    global expression
    while "*" in expression or "/" in expression:
        helper_index = index_in_dict("*", "/", expression)
        calc_func(expression[helper_index[0]], helper_index[0], expression)
        helper_index.pop(0)
    while "+" in expression or "-" in expression:
        helper_index = index_in_dict("+", "-", expression)
        calc_func(expression[helper_index[0]], helper_index[0], expression)
        helper_index.pop(0)




def index_in_dict(op1, op2, iterable):                #Возвращает список индексов двух указанных операторов в указываемом списке
    helper_index = []
    for i in range(len(iterable)):
        if iterable[i] == op1 or iterable[i] == op2:
            helper_index.append(i)
    return helper_index


def complex_converter():
    global expression
    for i in range(len(expression)):
        if "i" in expression[i]:
            expression[i] = re.sub('i', 'j', expression[i]) 
            for j in range(i-1, i+1):
                expression[i-2]+="".join(expression[j])
            for j in range(i-1, i+1):
                expression[j] = None
    while None in expression:
        expression.remove(None)
            
if __name__ == "__main__":
    expression = enter()
    complex_converter()
    while "(" in expression:
        left_index, right_index = bracket_finder()
        bracket_calc(left_index, right_index)
    while len(expression) > 2:
        main_calc()
    if expression[0].imag == 0j:
        print(expression[0].real)
    else:
        print(expression[0])




    
