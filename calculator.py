from tkinter import *
import math

class Main(Frame):
    formula: str

    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def press_key(event):
        print(event)

    # Создание функции окна для вывода вычислений
    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 20, "bold"), bg="green", foreground="white")
        self.lbl.place(x=10, y=30)

        # Создание кнопок
        btns = [
            "√2", "X^2", "|x|", "C", "DEL",
            "", "+/-", "n!", "mod", "/",
            "", "7", "8", "9", "*",
            "", "4", "5", "6", "-",
            "", "1", "2", "3", "+",
            "", "(", "0", ")", "="
        ]

        x = 10
        y = 100
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="orange",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=65,
                                      height=65)
            x += 80
            if x > 300:
                x = 10
                y += 70

    # Функция нахождения факториала
    def fac(self, operation):
        if self.formula == "n!":
            self.formula = str(math.factorial(int(self.formula)))
    # Функция вычисления операций калькулятора
    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula)) ** 2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        elif operation == "|x|":
            self.formula = str(abs(eval(self.formula)))
        elif operation == "n!":
            self.formula = str(math.factorial(int(self.formula)))
        elif operation == "√2":
            self.formula = str(math.sqrt(int(self.formula)))
        elif operation == "mod":
            self.formula = str(math.fmod(int(self.formula)))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "green"
    root.geometry("400x520")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
