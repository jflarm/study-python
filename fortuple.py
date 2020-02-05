#!/usr/bin/python3.7
list_of_points = [(1.6, 3.4), (5.3, 1.8), (7.5, 5.2)]
for x, y in list_of_points:
    print(f"x: {x}, y: {y}")
#diccionario como lista de tuplas
ages = dict([('juan', 13), ('jorge', 18), ('ana', 17)])
for name, age in ages.items():
    print (f"Person:  {name}")
    print (f"Age:  {age}")
#otro ejemplo de definicion de diccionatio    
list_people = {'jose':39, 'juan':29, 'angel':76}
for name, age in list_people.items():
    print (f"Person:  {name}")
    print (f"Age:  {age}")