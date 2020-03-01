#!/usr/bin/python3.7
name = ""
if not name:
    print("no name given")

#ejemplo de or
first = ""
last = "Martinez"
if first or last:
    print ("user has either first or last name")
#or tambien puede usarse para crear valores por defecto para variables
first = first or "juan"
print (first + " " + last)
prueba=False
if not prueba:
    print(prueba)