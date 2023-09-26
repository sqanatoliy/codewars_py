"""Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""
from typing import Literal

def bmi(weight, height) -> Literal['Underweight', 'Normal', 'Overweight', 'Obese'] | None:
    _bmi = weight / height**2
    if _bmi <= 18.5:
        return "Underweight"

    if _bmi <= 25.0:
        return "Normal"

    if _bmi <= 30.0:
        return "Overweight"

    if _bmi > 30:
        return "Obese"


if __name__=="__main__":
    print(bmi(80, 1.81))