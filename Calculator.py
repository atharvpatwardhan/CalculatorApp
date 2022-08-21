
from tkinter import Tk,Entry,Button,END

screen = Tk()
screen.geometry("370x500")
screen.title("Calculator")
screen.configure(bg="blue2")
entry = Entry(screen,bg = "gainsboro")
entry.place(x=10,y=10,width = 350,height = 70)


def click(num):
    currentnum = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(currentnum) + str(num))


def clear():
    entry.delete(0,END)

def addition():
    first_num = entry.get()
    global first_number
    global operation
    operation = "addition"
    first_number = int(first_num)
    entry.delete(0,END)

def subtract():
    first_num = entry.get()
    global first_number
    global operation
    operation = "subtraction"
    first_number = int(first_num)
    entry.delete(0,END)

def multiplication():
    first_num = entry.get()
    global first_number
    global operation
    operation = "multiplication"
    first_number = int(first_num)
    entry.delete(0,END)

def division():
    first_num = entry.get()
    global first_number
    global operation
    operation = "division"
    first_number = int(first_num)
    entry.delete(0,END)
    

def equal():
    second_number = entry.get()
    entry.delete(0,END)
    if operation == "addition" :
        entry.insert(0,first_number + int(second_number))
    elif operation == "subtraction" :
        entry.insert(0,first_number - int(second_number))
    elif operation == "multiplication" :
        entry.insert(0,first_number * int(second_number))
    elif operation == "division" :
        entry.insert(0,first_number / int(second_number))

zero_button = Button(text = "0" ,width = "10",height = "5",command =lambda : click(0),bg = "deep sky blue")
zero_button.place(x=10,y=400)

one_button = Button(text = "1",width = "10",height = "5",command =lambda : click(1),bg = "deep sky blue")
one_button.place(x=10,y=300)

two_button = Button(text = "2" ,width = "10",height = "5",command =lambda : click(2),bg = "deep sky blue")
two_button.place(x=100,y=300)

three_button = Button(text = "3" ,width = "10",height = "5",command =lambda : click(3),bg = "deep sky blue")
three_button.place(x=190,y=300)

four_button = Button(text = "4" ,width = "10",height = "5",command = lambda : click(4),bg = "deep sky blue")
four_button.place(x=10,y=200)

five_button = Button(text = "5" ,width = "10",height = "5",command = lambda : click(5),bg = "deep sky blue")
five_button.place(x=100,y=200)

six_button = Button(text = "6" ,width = "10",height = "5",command = lambda : click(6),bg = "deep sky blue")
six_button.place(x=190,y=200)

seven_button = Button(text = "7" ,width = "10",height = "5",command = lambda : click(7),bg = "deep sky blue")
seven_button.place(x=10,y=100)

eight_button = Button(text = "8" ,width = "10",height = "5",command = lambda : click(8),bg = "deep sky blue")
eight_button.place(x=100,y=100)

nine_button = Button(text = "9" ,width = "10",height = "5",command = lambda : click(9),bg = "deep sky blue")
nine_button.place(x=190,y=100)

plus_button = Button(text = "+" ,width = "10",height = "5" , command = addition,bg = "cyan")
plus_button.place(x=280,y=100)

minus_button = Button(text = "-" ,width = "10",height = "5",command = subtract,bg = "cyan")
minus_button.place(x=280,y=200)

multiplication_button = Button(text = "x" ,width = "10",height = "5",command = multiplication,bg = "cyan")
multiplication_button.place(x=280,y=300)

division_button = Button(text = "/" ,width = "10",height = "5",command = division,bg = "cyan")
division_button.place(x=280,y=400)

equate_button = Button(text = "=" ,width = "10",height = "5" , command = equal,bg = "cyan")
equate_button.place(x=190,y=400)

clear_button = Button(text = "C" ,width = "10",height = "5",command = clear,bg = "cyan")
clear_button.place(x=100,y=400)

screen.mainloop()

