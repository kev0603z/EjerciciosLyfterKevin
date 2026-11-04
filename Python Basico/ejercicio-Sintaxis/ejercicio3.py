# python ejercicio3.py

# Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random

current_number = random.randint(1, 10)
number = 0

while number != current_number:
    number = int(input( " Digite el numero secreto del 1 al 10 "))
    if number == current_number:
        print(f" Correcto!!!, El numero secreto es {current_number}")
    else:
        print(" Incorrecto!!!, Por favor intente de nuevo ")

