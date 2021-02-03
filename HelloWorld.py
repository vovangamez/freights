from tkinter import *
from PIL import ImageTk, Image

root=Tk()
canvas=Canvas(root, width=410, height=410)
canvas.pack()
PilImage=Image.open('1456378.jpg')
image=ImageTk.PhotoImage(PilImage)
imageSprite=canvas.create_image(400, 400, image=image)
root.mainloop()