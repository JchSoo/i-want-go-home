import tkinter
from PIL import ImageTk
import threading

window = tkinter.Tk()
window.title("I want to go home")
window.geometry("800x450+375+150")
window.resizable(False, False)

count = 0
state = ""

top = tkinter.Label(window, text = "집에 가고 싶을 때 마다 누르는 버튼")
top.pack()


def gui():

    def click():
        global count
        
        count += 1
        
        middle.config(text = f"{count}번 생각함")
        
        check()


    middle = tkinter.Label(window, text = f"{count}번 생각함")
    middle.pack()


    button = tkinter.Button(window, text = "아~ 집가고 싶다~!", command = click)
    button.pack()


    myimage = ImageTk.PhotoImage(file = "chaewon.png")
    bottom = tkinter.Label(window, image = myimage)
    bottom.pack()


    def change_a():
        global myimage

        myimage = ImageTk.PhotoImage(file = "chaewon.png")
        bottom.config(image = myimage)


    def change_b():
        global myimage2

        myimage2 = ImageTk.PhotoImage(file = "door1.png")
        bottom.config(image = myimage2)


    def change_c():
        global myimage3

        myimage3 = ImageTk.PhotoImage(file = "door2.png")
        bottom.config(image = myimage3)

    
    def change_d():
        global myimage4

        myimage4 = ImageTk.PhotoImage(file = "door3.png")
        bottom.config(image = myimage4)

    
    def change_e():
        global myimage5

        myimage5 = ImageTk.PhotoImage(file = "door4.png")
        bottom.config(image = myimage5)


    def change_f():
        global myimage6

        myimage6 = ImageTk.PhotoImage(file = "door5.png")
        bottom.config(image = myimage6)

    
    def change_g():
        global myimage7

        myimage7 = ImageTk.PhotoImage(file = "door6.png")
        bottom.config(image = myimage7)


    def change_h():
        global myimage8

        myimage8 = ImageTk.PhotoImage(file = "door7.png")
        bottom.config(image = myimage8)


    def change_i():
        global myimage9

        myimage9 = ImageTk.PhotoImage(file = "door8.png")
        bottom.config(image = myimage9)


    def change_j():
        global myimage10

        myimage10 = ImageTk.PhotoImage(file = "door9.png")
        bottom.config(image = myimage10)


    def dec():
        global count
        
        if count != 0:
            count -= 1
            check()
            middle.config(text = f"{count}번 생각함")
        
        threading.Timer(1, dec).start()


    def check():
        global count
        global state

        if count < 10 and state != "step1":
            change_a()
            state = "step1"
        
        if count >= 10 and count < 20 and state != "step2":
            change_b()
            state = "step2"
        
        if count >= 20 and count < 30 and state != "step3":
            change_c()
            state = "step3"

        if count >= 30 and count < 40 and state != "step4":
            change_d()
            state = "step4"

        if count >= 40 and count < 50 and state != "step5":
            change_e()
            state = "step5"

        if count >= 50 and count < 60 and state != "step6":
            change_f()
            state = "step6"

        if count >= 60 and count < 70 and state != "step7":
            change_g()
            state = "step7"

        if count >= 70 and count < 80 and state != "step8":
            change_h()
            state = "step8"

        if count >= 80 and count < 90 and state != "step9":
            change_i()
            state = "step9"

        if count >= 90 and count < 100 and state != "step10":
            change_j()
            state = "step10"

    dec()

    window.mainloop()

gui()