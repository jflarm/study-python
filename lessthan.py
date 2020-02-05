#!/usr/bin/python3.7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for num in a:
    if num < 5:
        print(num)
        b.append(num)
print(b)
#Codigo equivalente al for de arriba, pero solo con dos lineas en lugar de 6
c = [x for x in a if x < 5]
print(c)

#Preguntar a usuario limite superior
sup = input("Please, provide a number to set as upper limit: ")
d = [ y for y in a if y < int(sup)]
print(d)
#Resolviendo la impresion del arreglo en una sola linea
print([w for w in a if w < int(sup)])