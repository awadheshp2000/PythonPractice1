from typing import TypeVar, Generic
from tkinter import *

class Patient_load:

   def __init__(self,win):
        self.label1 =Label(win,text="Patient Name", fg='black', font=("Calibri", 12))
        self.label1.place(x=50, y=10)
        self.text1 = Entry(win,text="Patient Name", bd=4)
        self.text1.place(x=50, y=30)
        print(self.text1.get())

        self.label2 =Label(win,text="Patient Age", fg='black', font=("Calibri", 12))
        self.label2.place(x=300, y=10)
        self.text2 = Entry(win,text="Patient Age", bd=4)
        self.text2.place(x=300, y=30)

        self.label3 =Label(win,text="Height", fg='black', font=("Calibri", 12))
        self.label3.place(x=50, y=90)
        self.text3 = Entry(win,text="Height", bd=4)
        self.text3.place(x=50, y=110)

        self.label4 =Label(win,text="Weight", fg='black', font=("Calibri", 12))
        self.label4.place(x=300, y=90)
        self.text4 = Entry(win,text="Weight", bd=4)
        self.text4.place(x=300, y=110)

        self.button = Button(win,text="Save", fg="blue")
        self.button.place(x=225, y= 170)
        #self.button.bind('<Button-1>',save_patients())

    def save_patients(self):
        print(self.text1.get())
        print(self.text2.get())
        print(self.text3.get())
        print(self.text4.get())

windows = Tk()
Patient_load1 = Patient_load(windows)
windows.title("Patient Prediction")
windows.geometry("550x600")
windows.mainloop()
