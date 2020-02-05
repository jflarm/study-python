#Crear calculadora con cuatro funciones
#
#Funciones de calculadora
def sumar(a, b):
    if type(a) != int or type(b) != int:
        return False
    else: return a + b
    
def restar(a, b):
    if type(a) != int or type(b) != int:
        return False
    else: return a - b

def multiplicar(a, b):
    if type(a) != int or type(b) != int:
        return False
    else: return a * b

def dividir(a, b):
    if type(a) != int or type(b) != int:
        return False
    else: return a / b
#Menu:
    
while True:
    
    print('###### MENU #####')
    print('1) Sumar')
    print('2) Restar')
    print('3) multiplicar')
    print('4) Dividir' )
    
    try:
        option = int(input('>> '))
        if option < 4 or option > 1:
            break
    except ValueError:
        print("Opcion incorrecta! intentalo otra vez")
a = int(input("Primer numero: "))
b = int(input("Segundo Numero: "))  
if option is 1:
    print("Suma = " + str(sumar(a,b)))
elif option is 2:
    print("Resta = " + str(restar(a, b)))
elif option is 3:
    print("Multiplicacion = " + str(multiplicar(a, b)))
elif option is 4:
    print("Division = " + str(dividir(a, b)))

