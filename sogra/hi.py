import tkinter
from PIL import ImageTk


window = tkinter.Tk()
window.title("Do you want to go home")
window.geometry("800x450+375+150")
window.resizable(False, False)


top = tkinter.Label(window, text = "집 가고 싶을 때 누르는 버튼")
top.pack()


count = 0


def click():
    global count
    
    count += 1

    middle.config(text = f"{count}번 생각함")
    

middle = tkinter.Label(window, text = f"{count}번 생각함")
middle.pack()


button = tkinter.Button(window, text = "아~ 집가고 싶다~!", command = click)
button.pack()

# def picture():


myimage = ImageTk.PhotoImage(file = "chaewon.png")
label = tkinter.Label(window, image = myimage)
label.pack()


# def select(self):
#     value = "값 : " + str(scale.get())
#     label.config(text = value)

# var = tkinter.IntVar()

# scale = tkinter.Scale(window, variable = var, command = select, 
#                       orient = "horizontal", width = 10, bg = 'pink', 
#                       troughcolor = 'pink', sliderlength = 25, 
#                       tickinterval = 20, length = 300)
# scale.pack()

# label = tkinter.Label(window, text = "값 : 0")
# label.pack()


window.mainloop()