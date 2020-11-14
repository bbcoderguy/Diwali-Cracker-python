from PIL import Image, ImageSequence
import tkinter as tk
from tkinter import ttk
import os
from playsound import playsound
import threading as th
from time import sleep
from pygame import mixer

mixer.init()
root = tk.Tk()
root.geometry('400x300+500+200')
root.resizable(False,False)
root.title('...Happy Diwali... Dear Programmers')

img = tk.PhotoImage(file='Cracker.gif')
lbl = tk.Label(root,image=img,bg='black',cursor="@cursor.cur")
lbl.pack(fill='both')

im = Image.open("Cracker.gif")

def fire():
    global img
    index = 1
    root.attributes('-disabled', True)
    mixer.music.load('Sound4.mp3')
    mixer.music.play()
    for frame in ImageSequence.Iterator(im):
        frame.save("frame%d.png" % index)
        img = tk.PhotoImage(file="frame%d.png" % index)
        lbl.configure(image=img)
        lbl.update()
        os.remove("frame%d.png" % index)
        index += 1
    sleep(1)
    img = tk.PhotoImage(file='diwali.png')
    lbl.configure(image=img)
    lbl.update()
    sleep(3)
    img = tk.PhotoImage(file='Cracker.gif')
    lbl.configure(image=img)
    root.attributes('-disabled', False)

root.bind('<Button-1>',lambda x: fire())
root.mainloop()