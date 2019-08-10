#!/usr/bin/env python

"""
Display a png file and report the mouse position on a mouse click.
Todo:
  * Determine the image width and height. If small determine the resize factor
  * Run magick to convert and maybe resize the image

Shrink and convert JPG -> PNG

    magick convert rose.jpg -resize 50% rose.png
"""

from tkinter import *      

margin_x = 20
margin_y = 20

class MyApp:
    def __init__(self):
        root = Tk()      
        self.canvas = Canvas(root, width = 600, height = 400)      
        self.canvas.pack()      
        img = PhotoImage(file="ball.png")      
        self.canvas.create_image(margin_x, margin_y, anchor=NW, image=img)      


    def callback(self, event):  
        x = event.x - margin_x
        y = event.y - margin_y
        if x >= 0 and y >= 0:
            print("clicked at: ", x, y)


    def run(self):
        self.canvas.bind("<Button-1>", self.callback)
        mainloop()

def main():
    c = MyApp()
    c.run()

if __name__ == '__main__':
    main()
