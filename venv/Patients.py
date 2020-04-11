import psycopg2
from typing import TypeVar, Generic
from logging import Logger
from tkinter import *

class Cls_patients:

    def __init__ (self, patientname: str, address: str, age: float, Height: float, Weight: float)-> None:
        self.patientname = patientname
        self.address = address
        self. age = age
        self.Height = Height
        self.weight = Weight
        print (self.patientname)

    def set_customer(self)-> None:

        try:
            connection = psycopg2.connect(
                database="patientdatabase",
                user="postgres",
                passowrd="postgres",
                host="localhost",
                port="5432"
            )

            cursor = connection.cursor()
            postgresSQL_insert_query = 'insert into patients * from patients'
            cursor.execute(postgresSQL_insert_query)
            patients_records = cursor.fetchall()

            for row in patients_records:
                print (row[0])


        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
            print("PostgreSQL connection is closed")




customerdata = Cls_patients("Awadhesh", "Glasgow", 41, 171, 71)
customerdata.set_customer()



