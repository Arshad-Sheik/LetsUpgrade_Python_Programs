from pytube import YouTube
import os
from tkinter import *
from tkinter.messagebox import *


root=Tk()

w = 600 # width for the Tk root
h = 400 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Youtube Video Downloader Application')


Label_1 = Label(root,text="Paste The Youtube Link Below", font=("bold",26))
Label_1.place(x = 80, y = 100)


mylink = StringVar()

pastelink = Entry(root, width = 70, textvariable = mylink)
pastelink.place(x = 100, y = 180)

#link="https://www.youtube.com/watch?v=0NV1KdWRHck"

def downloadVideo():
    x = str(mylink.get())
    try:
        ytvideo = YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists('E:/Youtube Videos'):
            os.makedirs('E:/Youtube Videos')
        ytvideo.download('E:/Youtube Videos')
        pastelink.delete(0, END)
        
    except:
       print(showerror("ERROR", "Please Check your internet connection or Provide a valid youtube link to download"))
Button(root,text="Download Video", width=25, bg='green',fg="white", command=downloadVideo).place(x=210, y=240)

root.mainloop()