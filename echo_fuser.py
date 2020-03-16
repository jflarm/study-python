#!/usr/bin/env python3.7

def fuser(msg,times):
    if not times:
        times = '1'
    for i in range(int(times)):
        print(msg)

mensaje = input("Diga un mensaje: ")
qty = input("Diga la cantidad de veces que lo desea repetir: ").strip()

fuser(mensaje, qty)