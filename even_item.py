#!/usr/bin/python3.7
#Generate a new list with only the even items with one line of code
#Generar una nueva lista solo con los itemes pares con una sola linea de codigo

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([i for i in a if i % 2 == 0])

#more than one line / mas de una linea:
# new_list=[]
# for i in a:
#     if (int(i) % 2 == 0):
#         new_list.append(i)
# print(new_list)