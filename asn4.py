import tkinter
from PIL import Image, ImageTk


class MyGUI:
    def __init__(self):

        self.window = tkinter.Tk()
        self.window.title("food Viewer")

        self.x = tkinter.IntVar()

        self.top = tkinter.Frame(self.window)
        self.bottom = tkinter.Frame(self.window)

        self.b = Image.open("pie.jpg")
        self.b = self.b.resize((400,300))
        self.pic2 = ImageTk.PhotoImage(self.b)

        self.d = Image.open("steak.jpg")
        self.d = self.d.resize((300,300))
        self.pic4 = ImageTk.PhotoImage(self.d)

        self.a = Image.open("chicken.jpg")
        self.a = self.a.resize((400,300))
        self.pic1 = ImageTk.PhotoImage(self.a)

        self.c = Image.open("pizza.jpg")
        self.c = self.c.resize((350,300))
        self.pic3 = ImageTk.PhotoImage(self.c)

        self.x.set(1)

        self.btn2 = tkinter.Radiobutton(self.bottom, text="Pie", value=2, variable=self.x, command=self.on_radio_select)
        self.btn4 = tkinter.Radiobutton(self.bottom, text="Steak", value = 4, variable = self.x, command = self.on_radio_select)
        self.btn1 = tkinter.Radiobutton(self.bottom, text = "Chicken", value = 1, variable = self.x, command = self.on_radio_select)
        self.btn3 = tkinter.Radiobutton(self.bottom, text = "Pizza", value = 3, variable = self.x, command = self.on_radio_select)

        self.lbl = tkinter.Label(self.top, image = self.pic1)

        self.window.geometry("400x300")

        self.lbl.pack()
        self.top.pack()

        self.btn1.pack(side = "left", padx = 10)
        self.btn2.pack(side="left", padx=10)
        self.btn3.pack(side = "left", padx = 10)
        self.btn4.pack(side = "left", padx=10)

        self.bottom.pack()

        tkinter.mainloop()

    def on_radio_select(self):
        choice = self.x.get()

        if choice == 1:
            self.lbl.config(image = self.pic1)
        elif choice == 2:
            self.lbl.config(image=self.pic2)
        elif choice == 3:
            self.lbl.config(image = self.pic3)
        elif choice == 4:
            self.lbl.config(image=self.pic4)

if __name__ == '__main__':
    MyGUI()
