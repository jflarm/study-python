#!/usr/bin/env python3.7
#BMI (Body Mass Index)
#BMI= weight  in kg /(height in meters)squared
#Imperial version: BMI = 703 * BMI

def getInfo():
    height = float(input("Please, input height in meters or inches: "))
    weight = float(input("Please, input your weight in kilograms or pounds: "))
    system = input("Please, input the metric system, Imperial(feet and pounds) or Metric (meters and kilograms): ").lower()
    return (weight, height, system)

def calcBMI(weight, height, system="metric"):
    """
    This funcion calculates BMI (Body Mass Index) using the input
    parameters of weight, height and metric system
    """
    bmi = (weight / (height ** 2))
    if system == 'metric':
        return bmi
    else:
        if system == 'imperial':
            return (703 * bmi)

while True:

    weight, height, system = getInfo()
    if system == 'metric' or system == 'imperial':
        yourBMI = calcBMI(weight=weight,height=height,system=system)
        # print(f"Your BMI is {round(yourBMI,1)}")
        print(f"Your BMI is {yourBMI}")
    else:
        print("Wrong metric system")
        break
