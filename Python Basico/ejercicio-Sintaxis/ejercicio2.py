# python ejercicio2.py
# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, 
#niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.


name = (input(" Por favor digite su nombre "))
last_name = (input(" Por favor escriba su apellido "))
age = int(input(" Por favor digite su edad "))

if age <= 2:
    print (f" {name} {last_name} Usted es un bebe") 
elif age <= 10:
    print (f" {name}{last_name} Usted es un niño")
elif age <= 13:
    print (f" {name} {last_name} Usted es un preadolescente")
elif age <= 17:
    print (f" {name} {last_name} Usted es un adolescente")
elif age <= 23:
    print (f" {name} {last_name} Usted es un adulto joven ")
elif age <= 60:
    print (f" {name} {last_name} Usted es un adulto  ")
elif age <= 100:
    print (f" {name} {last_name} Usted es un adulto mayor ")
else:
    print (f" {name}   No puede tener mas de 1000 años")


