from typing import TypeVar
import Patient_Prediction

class test_patient_prediction:
    def test_sum():
        number1 = 400
        number2 =800
        number3 = 0
        Patient_Predict1 = Patient_Prediction.Patient_Predict()
        number3 = Patient_Predict1.sum(number1 , number2)
        assert number3 == 1200

