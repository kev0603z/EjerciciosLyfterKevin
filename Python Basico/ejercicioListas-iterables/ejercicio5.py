# python ejercicio5.py
# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

numbers = []
for index in range(10):
    single_number = int(input(f"Digite el número {index+1}: "))
    numbers.append(single_number)

print("list de numeros : ", numbers)

larger_number = numbers[0]  
for number in numbers:    
    if number > larger_number:   
        larger_number = number   

print("El número mayor es:", larger_number)
