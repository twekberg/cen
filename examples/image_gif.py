from tkinter import *      
root = Tk()      
canvas = Canvas(root, width = 300, height = 500)      
canvas.pack()      
img = PhotoImage(file="ball.gif")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()
