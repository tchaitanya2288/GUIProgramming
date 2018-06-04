from tkinter import *

root=Tk()
txt=Text(root)
txt.insert(INSERT,"Hello world")
txt.insert(END,"bye world")
txt.pack()

txt.tag_add("here","1.0","1.4")
txt.tag_add("start","1.8","1.11")
txt.tag_config("here",background="yellow",foreground="blue")
txt.tag_config("start",background="black",foreground="green")


root.mainloop()