import psycopg2
from typing import TypeVar, Generic
from logging import Logger


class Cls_patients():
    def __init__ (self, patientname: str, address: str, age: float, Height: float, Weight: float)-> None:
        self.patientname = patientname
        self.address = address
        self. age = age
        self.Height = Height
        self.weight = Weight
        print (self.patientname)

    def connection()-> None:
        conn = psycopg2.connect (
        database = "patientdatabase",
        user = "postgres",
        passowrd = "postgres",
        host = "localhost",
        port = "5432"
        )
Patients = Cls_patients("John Falcon", 'Glasgow', 41, 170, 72)




