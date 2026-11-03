#Experimente con el concepto de scope:
#Intente acceder a una variable definida dentro de una función desde afuera.
#ntente acceder a una variable global desde una función y cambiar su valor.

def fun_local():
    y = "solo dentro de la función"
    print("Dentro de la función:", y)

fun_local()

# Intento de acceder a la variable local desde afuera
# print(y)   # NameError: name 'y' is not defined

x = "kevin"

def fun():
    global x  
    x = "zuniga" 

fun()
print(x)
