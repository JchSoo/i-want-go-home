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

        if count < 100:
            count += 1
            middle.config(text = f"{count}번 생각함")
        
        check()

    middle = tkinter.Label(window, text = f"{count}번 생각함")
    middle.pack()

    button = tkinter.Button(window, text = "아~ 집가고 싶다~!", command = click)
    button.pack()

    myimage = ImageTk.PhotoImage(file = "./image/door0.png")
    bottom = tkinter.Label(window, image = myimage)
    bottom.pack()

    def ChangeImage(num):
        global myimage
        global state

        myimage = num
        state = num

        myimage = ImageTk.PhotoImage(file = f"./image/door{num}.png")
        bottom.config(image = myimage)

    def dec():
        global count
        
        if count > 0:
            count -= 1
            check()
            middle.config(text = f"{count}번 생각함")
        
        threading.Timer(1, dec).start()

    def check():
        global count
        global state
        thiscase = count // 10

        if state != thiscase:
            ChangeImage(thiscase)

    dec()

    window.mainloop()

gui()