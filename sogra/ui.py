import tkinter
from PIL import ImageTk
from tkinter import ttk
import threading
import tkinter.font
from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("I want to go home")
window.geometry("800x450+375+150")
window.resizable(False, False)
count = 0
state = ""
st = ""
font1=tkinter.font.Font(family="맑은 고딕", size=20, weight='bold')
top = tkinter.Label(window, text = "집에 가고 싶을 때 마다 누르는 버튼", font = font1)
top.pack()

def gui():
    font2=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")

    global button
    def click():
        global count
        global st
        global real
        if count < 100:
            count += 1
            check()
            prog_bar["value"] = count
            prog_bar.update()
        
        if count >= 100:
            count = 100
            prog_bar["value"] = count
            prog_bar.update()
            st = "1"
            button.configure(state = 'disabled')
            real = tkinter.Label(window, text = "되겠냐?", font = font2, state="active", activeforeground="red")
            real.pack()
            update(0)

    label = tkinter.Label(window)
    label.pack()

    prog_bar = ttk.Progressbar(window, length=300, maximum=100)
    prog_bar.pack()
    # prog_bar.grid(row=1, column=0, padx=10, pady=10)

    button = tkinter.Button(window, text = "아~ 집가고 싶다~!", command = click, width=20, height=2)
    button.pack()

    myimage = ImageTk.PhotoImage(file = "./image/door0.png")
    bottom = tkinter.Label(window, image = myimage)
    bottom.pack()

    def update(ind):
        global myimage
        global count
        global st
        global real
        
        ind += 1

        if ind < 10 and ind >= 0:
            myimage = ImageTk.PhotoImage(file = f"./suzume/suzume-000{ind}.jpg")
            bottom.config(image = myimage)
        elif ind < 96:
            myimage = ImageTk.PhotoImage(file = f"./suzume/suzume-00{ind}.jpg")
            bottom.config(image = myimage)
        else:
            myimage = ImageTk.PhotoImage(file = f"./image/door0.png")
            bottom.config(image = myimage)
            count = 0
            prog_bar["value"] = count
            prog_bar.update()
            st = ""
            button.configure(state = 'normal')
            real.pack_forget()
            return
        
        window.after(40, update, ind)

    def ChangeImage(num):
        global myimage
        global state

        myimage = num
        state = num

        myimage = ImageTk.PhotoImage(file = f"./image/door{num}.png")
        bottom.config(image = myimage)

    def dec():
        global st
        global count
        if count > 0 and st == "":
            count -= 1
            check()
            prog_bar["value"] = count
            prog_bar.update()
        a = 1 - (count / 110)
        threading.Timer(a, dec).start()

    def check():
        global count
        global state
        thiscase = (count // 2) * 2

        if state != thiscase:
            ChangeImage(thiscase)

    dec()

    window.mainloop()

if __name__ == '__main__':
    gui()