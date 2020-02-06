#!/usr/bin/python3.7
years_of_birth = [ 1986, 1982, 1976, 1996, 2001, 1945, 1967, 1998]
ages = []
import datetime
now = datetime.datetime.now()
datetime.datetime
datetime.date
cyear = now.year
# for year in years_of_birth:
#     ages.append(int(cyear) - year)
# print(ages)
#One line only
ages=[int(cyear) - i for i in years_of_birth]
# More than one line
# for i in years_of_birth:
#     ages.append(int(cyear) - i)
print(ages)