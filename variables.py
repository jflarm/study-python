#!/usr/bin/python3.7
# -*- coding: us-ascii -*-
charName = "Edward"
charAge = "30"
charJob = "teacher"
phrase = "estamos buscando la manera de aprender"
print(phrase)
print(charName + " is a very good guy")
print(charName + " is " + charAge + " years old")
print(charName + " is a " + charJob)
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[14])
print(phrase.index("aprender"))
print(phrase.replace("estamos","Nosotros estamos"))
print("Por defecto, la aritmetica del punto flotante puede dar valores extranos como el siguiente ejemplo de la operacion: -2.9 + (1 * 2 ):")
print(-2.9 + (1 * 2))
print("Por eso se puede usar la funcion round() para redondear con la cantidad de valores decimales deseados:")
print(round(-2.9 + (1 * 2),1))
#Modulous Operator
print(24 % 5)
#Convertir un numero a un string:
#Los numeros deben convertirse a string (texto) si se les quiere imprimir junto con texto
numero = 5
print("El numero que guarde en la variable es " + str(numero))

from math import *
#se pueden importar funciones especificas de una libreria
#from math import (floor,ceil,sqrt)
print(floor(3.5))
print(ceil(3.6))
print(sqrt(25))
#se puede redondear para quitar el punto decimal
print(floor(sqrt(25)))