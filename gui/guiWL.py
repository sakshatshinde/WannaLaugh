#import tkinter as tk
from tkinter import *
import os, winsound
from tkinter.ttk import *

bgVal = "#212121"
fgVal = "#ffeb3b"

root = Tk()
root.configure(background=bgVal, height = 700, width = 820)
root.resizable(FALSE, FALSE)

art = """

 ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▄ ▀▄  ▄▀▀█▄       ▄▀▀▀▀▄      ▄▀▀█▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▄  
█   █    ▐  █ ▐ ▄▀ ▀▄ █  █ █ █ █  █ █ █ ▐ ▄▀ ▀▄     █    █      ▐ ▄▀ ▀▄ █   █    █ █        █  █   ▄▀ 
▐  █        █   █▄▄▄█ ▐  █  ▀█ ▐  █  ▀█   █▄▄▄█     ▐    █        █▄▄▄█ ▐  █    █  █    ▀▄▄ ▐  █▄▄▄█  
  █   ▄    █   ▄▀   █   █   █    █   █   ▄▀   █         █        ▄▀   █   █    █   █     █ █   █   █  
   ▀▄▀ ▀▄ ▄▀  █   ▄▀  ▄▀   █   ▄▀   █   █   ▄▀        ▄▀▄▄▄▄▄▄▀ █   ▄▀     ▀▄▄▄▄▀  ▐▀▄▄▄▄▀ ▐  ▄▀  ▄▀  
         ▀    ▐   ▐   █    ▐   █    ▐   ▐   ▐         █         ▐   ▐              ▐         █   █    
                      ▐        ▐                      ▐                                      ▐   ▐    
"""

Label(root,text=art, font='TkFixedFont', background=bgVal, foreground=fgVal).place(x = 5,y = 0)



#playing music
winsound.PlaySound('extras/Goosebumps Theme Song (Caspro Remix).wav', winsound.SND_ALIAS | winsound.SND_LOOP + winsound.SND_ASYNC)
root.mainloop()
