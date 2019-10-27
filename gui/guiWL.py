
from tkinter import *
import os, winsound
from tkinter.ttk import *

bgVal = "#212121"
fgVal = "#fbc02d"

root = Tk()
root.configure(background=bgVal, height = 700, width = 820)
root.resizable(FALSE, FALSE)    #resizing turned off

#sets the window in center of the screen
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

#removes title bar and removes the ability to close the application from task bar
root.overrideredirect(True)

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
