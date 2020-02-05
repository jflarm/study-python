#!/usr/bin/python3.7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#4 lines program
# new_array=[]
# for x in a:
#      if x in b:
#         new_array.append(x)
# print(new_array)

#with one liner
print([x for x in a if x in b])

#Falta generar dos listas random y compararlas