from tkinter import Entry
from typing import TypeVar, Generic
import psycopg2
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

        self.button1 = Button(win,text="Save", fg="black")
        self.button1.bind('<Button-1>', self.save_patients)
        self.button1.place(x=175, y= 170)

        self.button2 = Button(win,text="Refresh", fg="black")
        self.button2.bind('<Button-1>',self.refresh)
        self.button2.place(x=325, y=170)

   def save_patients(self, event):
       try:
           connection1 = psycopg2.connect(
               database="patientdatabase",
               user="postgres",
               password="postgres",
               host="localhost",
               port="5432"
           )

           cursor = connection1.cursor()
           string1: str = str(self.text1.get())
           float1 = float(self.text2.get())
           float2 = float(self.text3.get())
           float3 = float(self.text4.get())

           cursor.execute("""insert into PatientMaster (Name, Age, Height, Weight) values ('%s', %f, %f, %f) """ % (string1, float1, float2, float3))
           connection1.commit()

       except (Exception, psycopg2.Error) as error:
           print("Error while fetching data from PostgreSQL", error)

       finally:
           # closing database connection.
           if (connection1):
               cursor.close()
               connection1.close()
           print("PostgreSQL connection is closed")


   def refresh(self,event):
       self.text1.delete(0,END)
       self.text2.delete(0,END)
       self.text3.delete(0,END)
       self.text4.delete(0,END)



windows = Tk()
Patient_load1 = Patient_load(windows)
windows.title("Patient Prediction")
windows.geometry("550x600")
windows.mainloop()
