from tkinter import *
import time
import base64
import os
from icon import img

def get_time():
    if mode == 'hour':
        timestr = time.strftime('%I:%M:%S %p')
    else:
        timestr = time.strftime('%b %d, %Y')
    lb.configure(text = timestr)
    root.after(1000, get_time)

def mouse_click(event):
    global mode
    if mode == 'hour':
        mode = 'day'
    else:
        mode = 'hour'

root = Tk()

tmp = open("tmp.ico","wb+")
tmp.write(base64.b64decode(img))
tmp.close()
root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

root.title('python-clock')
lb = Label(root, text='', bg = 'black', fg='white', font=("arial",100,'bold'))
lb.pack(anchor='center',fill = 'both', expand = 1)
lb.bind("<Button>", mouse_click)
mode = 'hour'
get_time()

root.mainloop()