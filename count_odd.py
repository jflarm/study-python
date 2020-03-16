#!/usr/bin/python3.7
limite = int(input("Indique el limete superior a evaluar pares: "))
count=0
while limite < 20:
    if count % 2 == 0:
        count += 1 #se le suma uno a la cuenta si el residuo de count/2 es 0
        continue #no sigue corriendo codigo dentro del while, por eso no es \
                 #necesario en el else, que es donde tambien termina el while.\
                 #Si se quiere terminar el while, se puede usar break
    else:
        print (f"We're counting odd numbers: {count}") #el caracter f permite \
        #insertar una variable en medio de str, esto se llama string interpola\
        #tion. Se imprime el numero primero, antes se aumentar la cuenta de \
        # count
        count +=1 #aumenta la cuenta
#Si no se aumenta la cuenta en ambas iteraciones del if, se incurre en un loop \
#infinito cuando se cae en esa rama del if
