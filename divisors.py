#!/usr/bin/python3.7
num = input("Input a number to find it's divisors: ")
# create array of possible divisors
#the range is num+1 because all numbers are divided by themselves, and the
#upper limit of the range is not part of the range itself, now it will show up
divs = []
for i in range(1, (int(num)) + 1):
    divs.append(i)

# print divisors (first attempt)
# for x in divs:
#     if int(num) % int(x) == 0:
#        print(x)

# #print divisors with two lines as an array (second attempt)
# d= [i for i in divs if int(num) % int(i) == 0]
# print(d)

# #print divisors with one line as an array (third attempt)
print([i for i in divs if int(num) % int(i) == 0])
