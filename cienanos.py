#!/usr/bin/python3.7
nom = input("Cual es tu nombre? ")
edad = input("Que edad tienes? ")
import datetime
tday = datetime.date.today()
#print(tday.year)
cien_en = int(tday.year) + int(edad)
print("Tendras 100 anos en el " + str(cien_en))


#Trabajar con fechas en python es raro, para encontrar año hay que declarar una\
#variable para la fecha de hoy y luego llamar un metodo para el año(year)