#!/usr/bin/env python3.7

def calc_bmi(weight, height, system="metric", rounded=False):
    """
    This funcion calculates BMI (Body Mass Index) using the input
    parameters of weight, height and metric system.
    calc_bmi(weigh=float/int,height=float/int,system=str(metric/imperial),rounded=bool(optional))
    """  
    if(system == 'metric' or system == 'imperial'):
        bmi = (weight / (height ** 2))

        if system == 'metric':
            if not rounded:
                return round(bmi,1)
            else:
                return round(bmi) 
        else:
            if system == 'imperial':
                if not rounded:
                    return round((703 * bmi),1)
                else:
                    return round((703 * bmi))        
    
    return 'Error: No valid system!'
    