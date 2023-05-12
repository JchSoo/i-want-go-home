import tkinter
from PIL import ImageTk

window = tkinter.Tk()
window.title("I want to go home")
window.geometry("800x450+375+150")
window.resizable(False, False)

top = tkinter.Label(window, text = "집 가고 싶을 때 누르는 버튼")
top.pack()

count = 0

def click():
    global count
    
    count += 1

    middle.config(text = f"{count}번 생각함")

    if count == 10:
        change_a()

    if count == 20:
        change_b()
    
middle = tkinter.Label(window, text = f"{count}번 생각함")
middle.pack()

button = tkinter.Button(window, text = "아~ 집가고 싶다~!", command = click)
button.pack()

myimage = ImageTk.PhotoImage(file = "chaewon.png")
bottom = tkinter.Label(window, image = myimage)
bottom.pack()

def change_a():
    global myimage2

    myimage2 = ImageTk.PhotoImage(file = "chaewon_two.png")
    bottom.config(image = myimage2)

def change_b():
    global myimage3

    myimage3 = ImageTk.PhotoImage(file = "kazuha.png")
    bottom.config(image = myimage3)

window.mainloop()