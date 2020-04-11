from typing import TypeVar, Generic
import Patient_Prediction

class test_patient_prediction:
    def test_sum():
        number1: float = 400
        number2: float =800
        number3: float
        number3 = Patient_Prediction.test_sum1(number1 + number2)
        print(number3)
        #assert number3 == 1200

