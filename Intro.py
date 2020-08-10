from  tkinter import *
from settings import *
from app_class import *
import tkinter.font as tkFont
state = "Intro"
root = Tk()
root.geometry("500x500")
global s
def play():
    a = App()
    a.run()
    print(entry.get())

root.configure(bg='black')
fontStyle  = tkFont.Font(family="Lucida Grande",size=30)
fontStyle1  = tkFont.Font(family="Lucida Grande",size=13)
fontStyle2  = tkFont.Font(family="Lucida Grande",size=20)
Label(root,text="WELCOME TO SUDOKU",fg="white",bg='black',width=25,font=fontStyle).pack()
label1 = Label(root,text="ENTER YOUR NAME",width=30,height=2,bg="black",fg='yellow',font=fontStyle2).place(x=20,y=85)
entry = Entry(root,width=30,bg="#2CFF00",fg='black',font=fontStyle1).place(x=110,y=150)
button = Button(root,text="PLAY",width=25,height=3,bg="#001FFF",fg="yellow",command=play).place(x=150,y=200)
button1 = Button(root,text="Quit",width=25,height=3,bg="#001FFF",fg="yellow", command=root.destroy).place(x=150,y=270)


if state == "Intro":
    mainloop()