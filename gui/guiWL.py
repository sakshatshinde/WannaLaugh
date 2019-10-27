#import tkinter as tk
from tkinter import *
import os, winsound
from tkinter.ttk import *


root = Tk()
root.resizable(False, False)

canvas = Canvas(root, height = 700, width = 820, bg = "#212121")

art = """

 ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▄ ▀▄  ▄▀▀█▄       ▄▀▀▀▀▄      ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▄  
█   █    ▐  █ ▐ ▄▀ ▀▄ █  █ █ █ █  █ █ █ ▐ ▄▀ ▀▄     █    █      ▐ ▄▀ ▀▄ █   █    █ █        █  █   ▄▀ 
▐  █        █   █▄▄▄█ ▐  █  ▀█ ▐  █  ▀█   █▄▄▄█     ▐    █        █▄▄▄█ ▐  █    █  █    ▀▄▄ ▐  █▄▄▄█  
  █   ▄    █   ▄▀   █   █   █    █   █   ▄▀   █         █        ▄▀   █   █    █   █     █ █   █   █  
   ▀▄▀ ▀▄ ▄▀  █   ▄▀  ▄▀   █   ▄▀   █   █   ▄▀        ▄▀▄▄▄▄▄▄▀ █   ▄▀     ▀▄▄▄▄▀  ▐▀▄▄▄▄▀ ▐  ▄▀  ▄▀  
         ▀    ▐   ▐   █    ▐   █    ▐   ▐   ▐         █         ▐   ▐              ▐         █   █    
                      ▐        ▐                      ▐                                      ▐   ▐    
"""

style = Style()
style.configure('Style.TButton', font='TkFixedFont', foreground="#dd2c00", bg="#212121")
label = Label(root,text=art, style='Style.TButton').place(x = 0,y = 0)

canvas.pack()

#playing music
winsound.PlaySound('extras/Goosebumps Theme Song (Caspro Remix).wav', winsound.SND_ALIAS | winsound.SND_LOOP + winsound.SND_ASYNC)
root.mainloop()
