import tkinter
from PIL import ImageTk
from tkinter import ttk
import threading
import tkinter.font
from typing import Final

window = tkinter.Tk()
window.title("I want to go home")
window.geometry("800x480+375+150")
window.resizable(False, False)
count = 0 
nowstate = 0 
gifplaying = False
font1=tkinter.font.Font(family="맑은 고딕", size=20, weight='bold')
top = tkinter   .Label(window, text = "집에 가고 싶을 때 마다 누르는 버튼", font = font1)
top.pack()
level = 1
cnt = 0

def gui():
    global button
    global level
    global cnt 
    up = 1
    up: Final

    def click():
        global count
        global gifplaying
        global real
        if count < 100:
            count += up
            check()
            prog_bar["value"] = count
            prog_bar.update()
        
        if count >= 100:
            count = 100
            prog_bar["value"] = count
            prog_bar.update()
            gifplaying = True
            button.configure(state = 'disabled')
            font2=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
            real = tkinter.Label(window, text = "되겠냐?", font = font2, state="active", activeforeground="red")
            real.pack()
            update(0)

    label = tkinter.Label(window)
    label.pack()

    prog_bar = ttk.Progressbar(window, length=300, maximum=100)
    prog_bar.pack()

    button = tkinter.Button(window, text = f"{level}레벨 아~ 집가고 싶다~!", command = click, width=20, height=2)
    button.pack()

    myimage = ImageTk.PhotoImage(file = "./image/door0.png")

    bottom = tkinter.Label(window, image = myimage)
    bottom.pack()

    def update(ind):
        global cnt
        global myimage
        global count
        global gifplaying
        global real
        global level
        
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
            gifplaying = False
            button.configure(state = 'normal')
            real.pack_forget()

            if level == 3:
                level = 1
                cnt += 1
                txt = 'Re' * cnt
                top.config(text = f"{txt}: 집에 가고 싶을 때 마다 누르는 버튼")
                button.config(text = f"{level}레벨 아~ 집가고 싶다~!")
                print(level)
            else:
                level += 1

                button.config(text = f"{level}레벨 아~ 집가고 싶다~!")
                print(level)

            return
        
        window.after(40, update, ind)

    def ChangeImage(num):
        global myimage
        global nowstate

        myimage = ImageTk.PhotoImage(file = f"./image/door{num}.png")
        bottom.config(image = myimage)

    def dec():
        global gifplaying
        global count
        global level

        if count > 0 and gifplaying == False: #횟수 0이상이고 스즈메 플레이 안하고 있으면
            count -= 1
            check()
            prog_bar["value"] = count
            prog_bar.update()

        tick = (4-level) - (count / 110)
        threading.Timer(tick, dec).start()

    def check():
        global count
        global nowstate

        thiscase = (count // 2) * 2

        if nowstate != thiscase: #이미지 바꿀 타이밍이면 바꿈
            ChangeImage(thiscase)

    dec()

    window.mainloop()

gui()