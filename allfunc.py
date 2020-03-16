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

def parse_list(lista):
    """
    parse_list(a) parses a list, creating three lists: strings, numbers and lists
    """
    numlist = []
    strlist = []
    listlist = []
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            numlist.append(i)
        elif isinstance(i, str):
            strlist.append(i)
        elif isinstance(i, list):
            listlist.append(i)
        else:
            pass
    return strlist, numlist, listlist

def num_count(lista):
    """
    num_count will add all numbers in a list
    and will count the numbers also.
    """
    total = 0
    items = 0
    for i in lista:
        if isinstance(i, int) or isinstance(i, float):
            total += i
            items += 1
        else:
            pass
    return total, items