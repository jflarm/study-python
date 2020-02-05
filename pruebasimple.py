#!/usr/bin/python3.7
myname = input("What is your name? ")
myage = input("What is your age? ")
import time
import datetime
time.sleep(1)
print("Hello, " + myname)
print("You are " + str(myage) + " years old")
print("You were born in " + str(2020 - int(myage)))
print("Today is " + str(datetime.date.today()))