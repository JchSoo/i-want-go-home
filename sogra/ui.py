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

        myimage2 = ImageTk.PhotoImage(file = "chaewon_two.png")
        bottom.config(image = myimage2)


    def change_c():
        global myimage3

        myimage3 = ImageTk.PhotoImage(file = "chaewon_three.png")
        bottom.config(image = myimage3)

    def dec():
        global count
        if count != 0:
            count -= 1
            check()
            middle.config(text = f"{count}번 생각함")
        threading.Timer(0.5, dec).start()

    def check():
        global count
        global state

        if count < 10 and state != "step1":
            change_a()
            state = "step1"
        if count >= 10 and count < 20 and state != "step2":
            change_b()
            state = "step2"
        if count > 20 and state != "step3":
            change_c()
            state = "step3"

    dec()

    window.mainloop()

gui()