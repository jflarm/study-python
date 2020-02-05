#!/usr/bin/python3.7
num = input("Input a number: ")
if int(num) % 4 == 0:
    print("Number is divisible by 4")
elif int(num) % 2 == 0 and int(num) % 4 != 0:
    print("Number is even")
else:
    print("Number is odd")
