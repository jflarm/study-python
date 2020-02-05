#!/usr/bin/python3.7
years_of_birth = [ 1986, 1982, 1976, 1996, 2001, 1945, 1967, 1998]
edades = []
import datetime
now = datetime.datetime.now()
cyear = now.year
for year in years_of_birth:
    edades.append(int(cyear) - year)
print(edades)