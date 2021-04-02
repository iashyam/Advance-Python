from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showerror
import os


class textEditor:
    def __init__(self):
        # Variables
        self.width = 700
        self.height = 500
        self.window = Tk()
        self.window.geometry(f'{self.width}x{self.height}')
        self.window.title('Text Editor')

        # a text area to enter the code
        self.text = StringVar()
        self.textarea = Text(self.window, width=self.width, height=self.height)
        self.textarea.config(font='20Arial')
        self.textarea.pack()

        # adding a menu
        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        # adding a file menu
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(menu=self.fileMenu, label='File')
        self.fileMenu.add_command(label="Save", command=self.save)
        self.fileMenu.add_command(label="Open", command=self.open)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=quit)

        #adding help menu
        self.helpmenu = Menu(self.menu, tearoff=0)
        self.helpmenu.add_command(label='Help', command=self.help)
        self.helpmenu.add_command(label='Documentation', command=self.help)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)

        #adding a run menu
        self.Runmenu = Menu(self.menu, tearoff=0)
        self.Runmenu.add_command(label='Build', command=self.help)
        self.Runmenu.add_command(label='Build and Run', command=self.help)
        self.menu.add_cascade(label="Run", menu=self.Runmenu)

        self.window.mainloop()

    def save(self):
        a = asksaveasfilename()
        if bool(a.strip()): #check if the file name is just spaces
            showerror(message="Please Enter a Valid file name")
        try:
            with open(a, 'w') as file:
                file.write(self.textarea.get('1.0', END))
        except Exception as e:
            showerror(message=str(e))

    def open(self):
        openFileName = askopenfilename()
        try:
            with open(openFileName, 'r') as file:
                line = file.read()
                self.textarea.delete('1.0', END)
                self.textarea.insert('1.0', line)
        except FileNotFoundError:
            showerror(message="File does not exists!")
    
    def help(self):
        pass


if __name__ == "__main__":
    textEditor()
