from os.path import basename, splitext
import tkinter as tk
from tkinter import Label, Button, Scale, Canvas
from tkinter.constants import HORIZONTAL

# from tkinter import ttk
class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Panel"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)  # kdyz dam esc tak quit

        self.lblR = tk.Label(self, text="R")
        self.lblR.pack()
        self.scaleR = Scale(from_=0, to=255, orient=HORIZONTAL, length=256, command=self.change) #red
        self.scaleR.pack()


        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = Scale(from_=0, to=255, orient=HORIZONTAL, length=256, command=self.change) # green
        self.scaleG.pack()


        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB = Scale(from_=0, to=255, orient=HORIZONTAL, length=256, command=self.change) #blue
        self.scaleB.pack()



        self.canvasMain=Canvas(width=256, height=100, background="#000000")
        self.canvasMain.pack()




        self.btn = tk.Button(self, text="Quit", command=self.quit) # odeji
        self.btn.pack()

        self.btn2 = tk.Button(self, text="About", command=self.quit) # o
        self.btn2.pack()

    
    
    def change(self, event):
        

        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()

        self.canvasMain.config(background=f"#{r:02x}{g:02x}{b:02x}")

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()   # mainloop