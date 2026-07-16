import tkinter as tk
import math

window = tk.Tk()
window.title("Calculator")

window.geometry("600x450")
window.resizable(1, 1)

for i in range(7):
    window.rowconfigure(i, weight=1)

window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=3)
window.columnconfigure(3, weight=2)
window.columnconfigure(4, weight=2)
window.columnconfigure(5, weight=3)
window.columnconfigure(6, weight=3)

angle_mode = tk.StringVar(value="Deg") 
inv_mode = tk.BooleanVar(value=False)  
last_answer = "0"                      

def press_num(num):
    text_in_box = entr_label.cget('text')
    if num == '.' and '.' in text_in_box:
        return
    entr_label.configure(text = text_in_box + str(num))

def press_op(operator):
    text_in_box = entr_label.cget('text')
    text_in_expr = expr_label.cget('text')
    expr_label.configure(text = text_in_expr + text_in_box + operator)
    entr_label.configure(text = '')

def press_C():
    expr_label.configure(text = '')
    entr_label.configure(text = '')

def press_eq():
    global last_answer
    text_in_box = entr_label.cget('text')
    text_in_expr = expr_label.cget('text')
    full_expr = text_in_expr + text_in_box
    expr_label.configure(text = full_expr + ' = ')
    try:
        full_expr = full_expr.replace('π', 'math.pi')
        full_expr = full_expr.replace('e', 'math.e')
        full_expr = full_expr.replace('EXP', '*10**')
        result = eval(full_expr)
        if isinstance(result, float):
            result = round(result, 8)
        last_answer = str(result)
        entr_label.configure(text = last_answer)
    except:
        entr_label.configure(text = 'ERROR !!!')

def press_trig(func_name):
    try:
        val = float(entr_label.cget('text'))
        if inv_mode.get(): 
            if func_name == 'sin':   res = math.asin(val)
            elif func_name == 'cos': res = math.acos(val)
            elif func_name == 'tan': res = math.atan(val)
            if angle_mode.get() == "Deg":
                res = math.degrees(res)
        else: 
            if angle_mode.get() == "Deg":
                val = math.radians(val)
            if func_name == 'sin':   res = math.sin(val)
            elif func_name == 'cos': res = math.cos(val)
            elif func_name == 'tan': res = math.tan(val)
        entr_label.configure(text=str(round(res, 8)))
    except:
        entr_label.configure(text='ERROR !!!')

def toggle_inv():
    inv_mode.set(not inv_mode.get())
    if inv_mode.get():
        inv_btn.configure(bg='#4C566A', fg='cyan')
    else:
        inv_btn.configure(bg='grey', fg='black')

def toggle_layout(selected_view):
    if selected_view == "Scientific":
        window.geometry("850x450") 
        for btn in sci_buttons:
            btn.grid() 
    else:
        window.geometry("600x450") 
        for btn in sci_buttons:
            btn.grid_remove()

expr_label = tk.Label(window, text = '', bg = 'grey', borderwidth = 3, relief = 'ridge', anchor = tk.E)
expr_label.grid(column = 0, row = 0, columnspan = 7, sticky=tk.NSEW)

entr_label = tk.Label(window, text = '', bg = 'grey', font = ('Arial bold', 15), borderwidth = 3, relief = 'ridge', anchor = tk.E)
entr_label.grid(column = 0, row = 1, columnspan = 7, sticky=tk.NSEW)

tk.Button(window, text = ' 7 ', fg = 'black', bg = 'grey', command= lambda: press_num(7)).grid(row=2, column = 0, sticky= tk.NSEW)
tk.Button(window, text = ' 8 ', fg = 'black', bg = 'grey', command= lambda: press_num(8)).grid(row=2, column = 1, sticky= tk.NSEW)
tk.Button(window, text = ' 9 ', fg = 'black', bg = 'grey', command= lambda: press_num(9)).grid(row=2, column = 2, sticky= tk.NSEW)
tk.Button(window, text = ' / ', fg = 'black', bg = 'grey', command= lambda: press_op('/')).grid(row=2, column = 3, sticky= tk.NSEW)
tk.Button(window, text = ' C ', fg = 'black', bg = 'grey', command = press_C).grid(row=2, column = 4, rowspan= 2, sticky= tk.NSEW)

tk.Button(window, text = ' 4 ', fg = 'black', bg = 'grey', command= lambda: press_num(4)).grid(row=3, column = 0, sticky= tk.NSEW)
tk.Button(window, text = ' 5 ', fg = 'black', bg = 'grey', command= lambda: press_num(5)).grid(row=3, column = 1, sticky= tk.NSEW)
tk.Button(window, text = ' 6 ', fg = 'black', bg = 'grey', command= lambda: press_num(6)).grid(row=3, column = 2, sticky= tk.NSEW)
tk.Button(window, text = ' * ', fg = 'black', bg = 'grey', command= lambda: press_op('*')).grid(row=3, column = 3, sticky= tk.NSEW)

tk.Button(window, text = ' 1 ', fg = 'black', bg = 'grey', command= lambda: press_num(1)).grid(row=4, column = 0, sticky= tk.NSEW)
tk.Button(window, text = ' 2 ', fg = 'black', bg = 'grey', command= lambda: press_num(2)).grid(row=4, column = 1, sticky= tk.NSEW)
tk.Button(window, text = ' 3 ', fg = 'black', bg = 'grey', command= lambda: press_num(3)).grid(row=4, column = 2, sticky= tk.NSEW)
tk.Button(window, text = ' - ', fg = 'black', bg = 'grey', command= lambda: press_op('-')).grid(row=4, column = 3, sticky= tk.NSEW)
tk.Button(window, text = ' = ', fg = 'black', bg = 'grey', command= press_eq).grid(row=4, column = 4, rowspan= 2, sticky= tk.NSEW)

tk.Button(window, text = ' 0 ', fg = 'black', bg = 'grey', command= lambda: press_num(0)).grid(row=5, column = 0, columnspan = 2, sticky= tk.NSEW)
tk.Button(window, text = ' . ', fg = 'black', bg = 'grey', command= lambda: press_num('.')).grid(row=5, column = 2, sticky= tk.NSEW)
tk.Button(window, text = ' + ', fg = 'black', bg = 'grey', command= lambda: press_op('+')).grid(row=5, column = 3, sticky= tk.NSEW)

view_mode = tk.StringVar(value="Normal")
mode_dropdown = tk.OptionMenu(window, view_mode, "Normal", "Scientific", command=toggle_layout)
mode_dropdown.config(bg='grey', font=('Arial', 8))
mode_dropdown.grid(row=0, column=0, columnspan=2, sticky='nw')

sci_buttons = []

deg_rb = tk.Radiobutton(window, text="Deg", variable=angle_mode, value="Deg", indicatoron=0, bg='grey', fg='black', selectcolor='#5E81AC')
rad_rb = tk.Radiobutton(window, text="Rad", variable=angle_mode, value="Rad", indicatoron=0, bg='grey', fg='black', selectcolor='#5E81AC')
deg_rb.grid(row=2, column=5, sticky=tk.NSEW)
rad_rb.grid(row=2, column=6, sticky=tk.NSEW)
sci_buttons.extend([deg_rb, rad_rb])

inv_btn = tk.Button(window, text="Inv", fg='black', bg='grey', command=toggle_inv)
sin_btn = tk.Button(window, text="sin", fg='black', bg='grey', command=lambda: press_trig('sin'))
inv_btn.grid(row=3, column=5, sticky=tk.NSEW)
sin_btn.grid(row=3, column=6, sticky=tk.NSEW)
sci_buttons.extend([inv_btn, sin_btn])

pi_btn = tk.Button(window, text="π", fg='black', bg='grey', command=lambda: press_num('π'))
cos_btn = tk.Button(window, text="cos", fg='black', bg='grey', command=lambda: press_trig('cos'))
pi_btn.grid(row=4, column=5, sticky=tk.NSEW)
cos_btn.grid(row=4, column=6, sticky=tk.NSEW)
sci_buttons.extend([pi_btn, cos_btn])

e_btn = tk.Button(window, text="e", fg='black', bg='grey', command=lambda: press_num('e'))
tan_btn = tk.Button(window, text="tan", fg='black', bg='grey', command=lambda: press_trig('tan'))
e_btn.grid(row=5, column=5, sticky=tk.NSEW)
tan_btn.grid(row=5, column=6, sticky=tk.NSEW)
sci_buttons.extend([e_btn, tan_btn])

ans_btn = tk.Button(window, text="Ans", fg='black', bg='grey', command=lambda: press_num(last_answer))
exp_btn = tk.Button(window, text="EXP", fg='black', bg='grey', command=lambda: press_op('EXP'))
ans_btn.grid(row=6, column=5, sticky=tk.NSEW)
exp_btn.grid(row=6, column=6, sticky=tk.NSEW)
sci_buttons.extend([ans_btn, exp_btn])

for btn in sci_buttons:
    btn.grid_remove()

window.mainloop()
