from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry("500x500")

def hellocallback():
    msg=messagebox.showinfo("Home","Welcome to Python")

btn=Button(top,text="Click to begin",command=hellocallback)
btn.place(x=200,y=450)
top.mainloop()
