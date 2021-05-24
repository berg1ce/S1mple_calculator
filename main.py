import tkinter as tk


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
# Функция вычисления операций калькулятора
def calculate(operation: object, label_text=None):
    global formula, buttons

    if operation == 'C':
        formula = ''
    elif operation == 'def':
        formula = formula[0: -1]
    elif operation == 'X^2':
        formula = str((eval(formula)) ** 2)
    elif operation == '=':
        formula = str((eval(formula)))
    else:
        if formula == '0':
            formula = ''
            formula += operation
            label_text.configure(text=formula)


            # Создание окна для вывода вычислений
            formula = '0'
            label_text = tk.Label(text=formula, font=('Roboto', 20, 'bold'), bg='black', fg='white')
            label_text.place(x=11, y=50)


            # Создание кнопок
            buttons = ['C', 'def', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '+/-', '0',
                       '%', 'X^2']
        x = 10
        y = 140
        for button in buttons:
            get_lbl = lambda x=button: calculate(x)
            tk.Button(text=button, bg='orange', font=('Roboto', 15), command=get_lbl).place(x=x, y=y, width=115, height=79)
        x += 117
        if x > 400:
            x = 10
            y += 81

window = tk.Tk()
window.title('Calculator')
window.geometry('485x550+200+200')
window.resizable(False, False)
window.configure(bg='green')
window.mainloop()

