#!/usr/bin/python3.7
colors = ['blue','green','red','yellow','purple']
for color in colors:
    print(color)
    if color == 'yellow':
        break
    #se imprimen todos los colores, pero al imprimir yellow, cumple con la con\
    #dicion de color=='yellow' y hace un break, saliendo del for y no se imprime\
    #purple