import tkinter as tk

window = tk.Tk()
window.title("Soapy Calculator")
window.geometry("400x400")

def yippee():
    print("Yippee!")
    
def display_text() -> None:
    global result
    text = text_inp.get()
    print(text)
    result.config(text=text)
    return None

keypad = tk.Frame(name="keypad_frame", border=10, height=100, width=100, background="gray")

"""
[1][2][3][+]
[4][5][6][-]
[7][8][9][*]
[.][0][=][/]
"""

def is_number(value):
    if value == "\u03C0": # \u03C0 is pi
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

def find_precedence(operator) -> int:
    match operator:
        case '^':
            return 3
        case '*' | '/':
            return 2
        case '+' | '-':
            return 1
        case _:
            return 0

def shunting_yard(infix_notation: list) -> list:
    """Converts the input infix notation to a more usable postfix notation using the Shunting Yard algorithm.
    """

    operators = ['^', '']

    stack = []
    queue = []

    for item in infix_notation:
        if is_number(item): # if it is a number
            queue.append(item)
        elif item in operators == 0: # if it is an operator
            # i fucking give up for now :3
        elif item != ")":
            stack.append(item)



    postfix_notation = []

    return postfix_notation
    
def calculate_answer(formula):
    output_str = "".join(formula)
    print(output_str)

formula = []

def draw_formula(formula: list) -> None:
    if len(formula) > 0:
        joined = "".join(formula)
    else:
        joined = "0"
    formula_label.config(text=joined) # update the formula on the display

def handle_input(button):
    global formula
    
    button = str(button)
    
    match button:
        case "=":
            calculate_answer(formula)
        case ".":
            if len(formula) > 0:
                if is_number(formula[-1]+"."):
                    formula[-1] += "."
        case _:
            if len(formula) > 0:
                if is_number(button) and is_number(formula[-1]):
                    formula[-1] += button
                elif not is_number(button) and is_number(formula[-1]):
                        formula[-1] = formula[-1].removesuffix(".")
                        formula.append(button)
                elif not is_number(formula[-1]) and is_number(button):
                    formula.append(button)
                else:
                    formula[-1] = button
            else:
                if is_number(button):
                    formula.append(button)
    draw_formula(formula)
    # print(formula)

formula_label = tk.Label(text="0", font=("TkDefaultFont, 15"), master=keypad, height=2, width=18)
formula_label.grid(column=0, row=0, columnspan=4, padx=5, pady=5)

button_1 = tk.Button(text="1", command=lambda: handle_input(1), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=0, row=1)
button_2 = tk.Button(text="2", command=lambda: handle_input(2), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=1, row=1)
button_3 = tk.Button(text="3", command=lambda: handle_input(3), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=2, row=1)
button_4 = tk.Button(text="4", command=lambda: handle_input(4), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=0, row=2)
button_5 = tk.Button(text="5", command=lambda: handle_input(5), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=1, row=2)
button_6 = tk.Button(text="6", command=lambda: handle_input(6), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=2, row=2)
button_7 = tk.Button(text="7", command=lambda: handle_input(7), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=0, row=3)
button_8 = tk.Button(text="8", command=lambda: handle_input(8), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=1, row=3)
button_9 = tk.Button(text="9", command=lambda: handle_input(9), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=2, row=3)
button_0 = tk.Button(text="0", command=lambda: handle_input(0), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=1, row=4)

dot_button = tk.Button(text=".", command=lambda: handle_input("."), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=0, row=4)
equal_button = tk.Button(text="=", command=lambda: handle_input("="), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=2, row=4)

add_button = tk.Button(text="+", command=lambda: handle_input("+"), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=3, row=1)
min_button = tk.Button(text="-", command=lambda: handle_input("-"), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=3, row=2)
mul_button = tk.Button(text="*", command=lambda: handle_input("x"), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=3, row=3)
div_button = tk.Button(text="÷", command=lambda: handle_input("÷"), font=("TkDefaultFont", 15), master=keypad, height=2, width=4).grid(column=3, row=4)

keypad.grid()

text_inp = tk.Entry(master=keypad, width=50, border=2, bg="gray")



window.mainloop()