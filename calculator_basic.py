import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("450x600+300+300")
root.resizable(100, 100)
root.title("Anton")


val = ""
A = 0
operator = ""

class btn_clicked:
    def __init__(self):
        pass

    @staticmethod
    def btn_1_isclicked():
        global val
        val = val + "1"
        data.set(val)

    @staticmethod
    def btn_2_isclicked():
        global val
        val = val + "2"
        data.set(val)

    @staticmethod
    def btn_3_isclicked():
        global val
        val = val + "3"
        data.set(val)

    @staticmethod
    def btn_4_isclicked():
        global val
        val = val + "4"
        data.set(val)

    @staticmethod
    def btn_5_isclicked():
        global val
        val = val + "5"
        data.set(val)

    @staticmethod
    def btn_6_isclicked():
        global val
        val = val + "6"
        data.set(val)

    @staticmethod
    def btn_7_isclicked():
        global val
        val = val + "7"
        data.set(val)

    @staticmethod
    def btn_8_isclicked():
        global val
        val = val + "8"
        data.set(val)

    @staticmethod
    def btn_9_isclicked():
        global val
        val = val + "9"
        data.set(val)

    @staticmethod
    def btn_0_isclicked():
        global val
        val = val + "0"
        data.set(val)

    @staticmethod
    def btn_plus_isclicked():
        global A, val, operator
        A = int(val)
        operator = "+"
        val = val + "+"
        data.set(val)

    @staticmethod
    def btn_sub_isclicked():
        global A, val, operator
        A = int(val)
        operator = "-"
        val = val + "-"
        data.set(val)

    @staticmethod
    def btn_mul_isclicked():
        global A, val, operator
        A = int(val)
        operator = "*"
        val = val + "*"
        data.set(val)

    @staticmethod
    def btn_div_isclicked():
        global A, val, operator
        A = int(val)
        operator = "/"
        val = val + "/"
        data.set(val)

    @staticmethod
    def btn_ac_isclicked():
        global A, val, operator
        A = 0
        operator = ""
        val = ""
        data.set(val)

    @staticmethod
    def btn_result():
        global A, val, operator
        val2 = val
        if operator == "+":
            x = int(val2.split("+")[1])
            c = A+x
            data.set(c)
            val=str(c)
        elif operator == "-":
            x = int(val2.split("-")[1])
            c = A - x
            data.set(c)
            val = str(c)
        elif operator == "*":
            x = int(val2.split("*")[1])
            c = A * x
            data.set(c)
            val = str(c)
        elif operator == "/":
            x = int(val2.split("/")[1])
            if operator == 0:
                messagebox.showerror("ERROR", "Divisible by 0 not supported!")
                A = ""
                val = ""
                data.set(val)
            else:
                c = int(A/x)
                data.set(c)
                val=str(c)


clicked = btn_clicked


def label():
    global data
    data =StringVar()
    lbl = Label(
        root,
        text="Label",
        anchor=SE,
        font= ("veranda", 40),
        textvariable= data,
        background = "#ffffff",
        fg = "#000000",
    )
    lbl.pack(expand = True, fill = "both")
label()

def row1():
    btnrow1 = Frame(root)
    btnrow1.pack(expand = True, fill = "both")

    btn_mod = Button(
        btnrow1,
        text="%",
        font=("veranda", 22),
        relief=GROOVE,
        border= 0
    )
    btn_mod.pack(expand=True, fill="both", side="left")

    btn_CE = Button(
        btnrow1,
        text="CE",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_ac_isclicked,
    )
    btn_CE.pack(expand=True, fill="both", side="left")

    btn_C = Button(
        btnrow1,
        text="C",
        font=("veranda", 22),
        relief=GROOVE,
        border=0
    )
    btn_C.pack(expand=True, fill="both", side="left")

    #photo = PhotoImage(file=r"C:\Users\Samiul Islam Anton\PycharmProjects\Calculator\back.png")
    #photoimage = photo.subsample(2,2)
    btn_back = Button(
        btnrow1, #image = photo,
        text = "p",
        font=("veranda", 20),
        relief = GROOVE,
        border = 0
    )
    btn_back.pack(expand=True, fill="both", side="left")
row1()

def row2():
    btnrow2 = Frame(root)
    btnrow2.pack(expand = True, fill = "both")
    btn_1x = Button(
        btnrow2,
        text="1/x",
        font=("veranda", 22),
        relief=GROOVE,
        border=0
    )
    btn_1x.pack(expand=True, fill="both", side="left")

    btn_xx = Button(
        btnrow2,
        text="x2",
        font=("veranda", 22),
        relief=GROOVE,
        border=0
    )
    btn_xx.pack(expand=True, fill="both", side="left")

    btn_2rootx = Button(
        btnrow2,
        text="2~x",
        font=("veranda", 22),
        relief=GROOVE,
        border=0
    )
    btn_2rootx.pack(expand=True, fill="both", side="left")

    # photo = PhotoImage(file=r"C:\Users\Samiul Islam Anton\PycharmProjects\Calculator\back.png")
    # photoimage = photo.subsample(2,2)
    btn_div = Button(
        btnrow2,  # image = photoimage,
        text="/",
        font=("veranda", 20),
        relief = GROOVE,
        border = 0,
        command = clicked.btn_div_isclicked,
    )
    btn_div.pack(expand=True, fill="both", side="left")
row2()

def row3():
    btnrow3 = Frame(root)
    btnrow3.pack(expand = True, fill = "both")
    btn7 = Button(
        btnrow3,
        text="7",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_7_isclicked,
    )
    btn7.pack(expand=True, fill="both", side="left")

    btn8 = Button(
        btnrow3,
        text="8",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_8_isclicked,
    )
    btn8.pack(expand=True, fill="both", side="left")

    btn9 = Button(
        btnrow3,
        text="9",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_9_isclicked,
    )
    btn9.pack(expand=True, fill="both", side="left")

    btn_mul = Button(
        btnrow3,
        text="*",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_mul_isclicked,
    )
    btn_mul.pack(expand=True, fill="both", side="left")
row3()

def row4():
    btnrow4 = Frame(root)
    btnrow4.pack(expand = True, fill = "both")

    btn4 = Button(
        btnrow4,
        text="4",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_4_isclicked,
    )
    btn4.pack(expand=True, fill="both", side="left")

    btn5 = Button(
        btnrow4,
        text="5",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_5_isclicked,
    )
    btn5.pack(expand=True, fill="both", side="left")

    btn6 = Button(
        btnrow4,
        text="6",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_6_isclicked,
    )
    btn6.pack(expand=True, fill="both", side="left")

    btn_sub = Button(
        btnrow4,
        text="-",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_sub_isclicked,
    )
    btn_sub.pack(expand=True, fill="both", side="left")
row4()

def row5():
    btnrow5 = Frame(root)
    btnrow5.pack(expand = True, fill = "both")

    btn1 = Button(
        btnrow5,
        text="1",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_1_isclicked,
    )
    btn1.pack(expand=True, fill="both", side="left")

    btn2 = Button(
        btnrow5,
        text="2",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_2_isclicked,
    )
    btn2.pack(expand=True, fill="both", side="left")

    btn3 = Button(
        btnrow5,
        text="3",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_3_isclicked,
    )
    btn3.pack(expand=True, fill="both", side="left")

    btn_add = Button(
        btnrow5,
        text="+",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_plus_isclicked,
    )
    btn_add.pack(expand=True, fill="both", side="left")
row5()

def row6():
    btnrow6 = Frame(root)
    btnrow6.pack(expand = True, fill = "both")

    btn_AC = Button(
        btnrow6,
        text="AC",
        font=("veranda", 12),
        relief=GROOVE,
        border=0,
        command = clicked.btn_ac_isclicked,
    )
    btn_AC.pack(expand=True, fill="both", side="left")

    btn0 = Button(
        btnrow6,
        text="0",
        font=("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_0_isclicked,
    )
    btn0.pack(expand=True, fill="both", side="left")

    btn_dot = Button(
        btnrow6,
        text=".",
        font=("veranda", 22),
        relief=GROOVE,
        border=0
    )
    btn_dot.pack(expand=True, fill="both", side="left")

    btn_equal = Button(
        btnrow6,
        text="=",
        font = ("veranda", 22),
        relief=GROOVE,
        border=0,
        command = clicked.btn_result,
    )
    btn_equal.pack(expand=True, fill="both", side="left")
row6()


root.mainloop()