from typing import TypeVar, Generic
from Patient_Prediction import Patient_Prediction

class test_patient_prediction:
    def test_sum():
        number1: float = 400
        number2: float =800
        number3: float
        Patient_Prediction1 = Patient_Prediction
        number3 = Patient_Prediction1.test_sum1(number1+number2)
        print(number3)
        print("Hi")
        #assert number3 == 1200

test_patient_prediction1 = test_patient_prediction
test_patient_prediction1.test_sum()