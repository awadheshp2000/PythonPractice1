from typing import TypeVar, Generic
import Patient_Prediction

class test_Patient_Prediction:
    def test_sum():
        number1: float = 400
        number2: float =800
        number3: float
        number3 = test_sum(number1 + number2)
        assert number3 == 1200


