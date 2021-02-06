from tkinter import *
from functools import partial

def clear_all():
    display.delete(0, len(display.get()))
    display.insert(0, 0)

def clear():
    display.delete(len(display.get())-1)
    if display.get() == '':
        display.insert(0, 0)

def place_number(value):
    if display.get() == '0' or display.get() == "Invalid":
        display.delete(0, len(display.get()))
    display.insert(len(display.get()), value)

def place_operator(value):
    if display.get()[-1] in operators:
        display.delete(len(display.get())-1)
    if display.get() == 'Invalid':
        display.delete(0, len(display.get()))
        display.insert(len(display.get()), 0)
    display.insert(len(display.get()), value)

def place_bracket(value):
    if value == '(':
        if display.get()[-1] == '(':
            return
        else:
            display.insert(len(display.get()), '*(')
    if value == ')':
        if display.get()[-1] == '(':
            display.delete(len(display.get())-1)
        elif display.get()[-1] == '(':
            display.delete(len(display.get())-1)
            display.insert(len(display.get()), ')')
        else:
            display.insert(len(display.get()), ')')

def display_answer():
    exp = display.get()
    try:
        value = eval(exp)
    except:
        value = 'Invalid'
    display.delete(0 , len(display.get()))
    display.insert(0, value)

calc = Tk()
calc.title('Calculator')
calc.resizable(False, False)
calc.config(bg='light blue')
calc.geometry('332x381+100+100')

numbers = '789456123'
operators = '+-*/'
brackets = '()'

display = Entry(calc, width=19, font=('ebrima', 21, 'bold'), bg='#5e9edd', fg='white', bd=13, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4)
display.insert(0, 0)

btn_ac = Button(calc, text='CE', width=5, font=('ebrima', 20), bg='#5e9edd', activebackground='light blue',
fg='white', bd=0, relief=FLAT, command=clear_all)
btn_ac.grid(row=1, column=0, padx=1, pady=1)

btn_clear = Button(calc, text='C', width=5, font=('ebrima', 20), bg='#5e9edd', activebackground='light blue',
fg='white', bd=0, relief=FLAT, command=clear)
btn_clear.grid(row=1, column=1, padx=1, pady=1)

btn_equal = Button(calc, text='=', width=5, font=('ebrima', 20), bg='#5e9edd', activebackground='light blue',
fg='white', bd=0, relief=FLAT, command=display_answer)
btn_equal.grid(row=1, column=2, padx=1, pady=1)

for i in range(9):
    btn = Button(calc, text=numbers[i], width=5, font=('ebrima', 20), bg='white', bd=0, relief=FLAT,
    command=partial(place_number, numbers[i]))
    btn.grid(row=i//3+2, column=i%3, padx=1, pady=1)

for i in range(4):
    btn = Button(calc, text=operators[i], width=5, font=('ebrima', 20), bg='#5e9edd', activebackground='light blue', fg='white', bd=0, relief=FLAT, command=partial(place_operator, operators[i]))
    btn.grid(row=i+1, column=3, padx=1, pady=1)

btn_dot = Button(calc, text='.', width=5, font=('ebrima', 20), bg='#5e9edd', activebackground='light blue',
fg='white', bd=0, relief=FLAT, command=partial(place_number, '.'))
btn_dot.grid(row=5, column=0, padx=1, pady=1)

btn_zero = Button(calc, text='0', width=5, font=('ebrima', 20), bg='#5e9edd', activebackground='light blue',
fg='white', bd=0, relief=FLAT, command=partial(place_number, 0))
btn_zero.grid(row=5, column=1, padx=1, pady=1)

for i in range(2):
    btn = Button(calc, text=brackets[i], width=5, font=('ebrima', 20), bg='#5e9edd', activebackground='light blue',
    fg='white', bd=0, relief=FLAT, command=partial(place_bracket, brackets[i]))
    btn.grid(row=5, column=i+2, padx=1, pady=1)
    
calc.mainloop()