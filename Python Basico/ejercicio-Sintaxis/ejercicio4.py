# python ejercicio4.py

# Cree un programa que le pida tres números al usuario y muestre el mayor.

number = int(input(" Por favor digite el numero #1 "))
number2 = int(input(" Por favor digite el numero #2 "))
number3 = int(input(" Por favor digite el numero #3 "))


if number > number2 and number > number3:
    print (f" El numero mayor es el numero: {number}")
elif number2 > number and number2 > number3:
    print (f" El numero mayor es el numero: {number2}")
elif number3 > number and number3 > number2:
    print (f" El numero mayor es el numero: {number3}")

