from os.path import basename, splitext
import tkinter as tk
from tkinter import Label, Button, Scale, Canvas, Frame, Entry , LEFT, S, StringVar
from tkinter.constants import HORIZONTAL

# from tkinter import ttk
class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Panel"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)  # kdyz dam esc tak quit
        
        self.varR = StringVar()
        self.frameR = Frame(self)
        self.frameR.pack()

        self.lblR = tk.Label(self.frameR, text="R")
        self.lblR.pack(side=LEFT, anchor =S)
        self.scaleR = Scale(self.frameR,from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varR ) #red
        self.scaleR.pack(side=LEFT, anchor =S)
        self.entryR = Entry(self.frameR, width =5, textvariable=self.varR)
        self.entryR.pack(side=LEFT, anchor =S)
        
        self.varG = StringVar()
        self.frameG = Frame(self)
        self.frameG.pack()

        self.lblG = tk.Label(self.frameG, text="G")
        self.lblG.pack(side = LEFT, anchor =S)
        self.scaleG = Scale(self.frameG, from_=0, to=255, orient=HORIZONTAL, length=256,  variable=self.varG) # green
        self.scaleG.pack(side = LEFT, anchor =S)
        self.entryG = Entry(self.frameG, width =5, textvariable=self.varG)
        self.entryG.pack(side = LEFT, anchor =S)
        
        self.varB = StringVar()
        self.frameB = Frame(self)
        self.frameB.pack()

        self.lblB = tk.Label(self.frameB, text="B")
        self.lblB.pack(side = LEFT, anchor =S)
        self.scaleB = Scale(self.frameB, from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varB) #blue
        self.scaleB.pack(side = LEFT, anchor =S)
        self.entryB = Entry(self.frameB, width =5, textvariable=self.varB)
        self.entryB.pack(side = LEFT, anchor =S)


        self.canvasMain=Canvas(width=256, height=100, background="#000000")
        self.canvasMain.pack()
        self.canvasMain.bind("<Button-1>",self.mousehandler)

        self.varMain = StringVar()
        self.entryMain = Entry(
            self,
            textvariable = self.varMain,
            state ="readonly",
            readonlybackground = "#fff",
        )
        self.entryMain.pack()



        self.btn = tk.Button(self, text="Quit", command=self.quit) # odeji
        self.btn.pack()

        self.btn2 = tk.Button(self, text="About", command=self.quit) # o
        self.btn2.pack()

        self.varR.trace("w", self.change)              # Na to aby to sledovalo tu změnu při manual napsání rozsahu 
        self.varG.trace("w", self.change)
        self.varB.trace("w", self.change)

        self.frameMem = Frame(self)
        self.frameMem.pack()
        self.canvasMem = []
        for row in range(3):
            for column in range (7):
                canvas = Canvas (self.frameMem ,width=50, height=50, background="#abcdef") 
            
                canvas.grid(row =row, column =column)
                canvas.bind("<Button-1>",self.mousehandler)
                self.canvasMem.append(canvas)
    
    def mousehandler(self, event):
        #print(dir(event))
        if self.cget("cursor")!="pencil" :
            self.config(cursor="pencil")
            self.color = event.widget.cget("background")
        elif self.cget("cursor") == "pencil" :
            self.config(cursor="")
            event.widget.config(background=self.color)
    
    def change(self, var,index, mode):
        

        r = int(self.scaleR.get())
        g = int(self.scaleG.get())
        b = int(self.scaleB.get())

        self.canvasMain.config(background=f"#{r:02x}{g:02x}{b:02x}")
        self.varMain.set(f"#{r:02x}{g:02x}{b:02x}")
        # self.varR.set(r)
        # self.varG.set(g)
        # self.varB.set(b)

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()   # mainloop
