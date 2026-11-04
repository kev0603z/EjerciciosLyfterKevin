# python ejercicio4.py
# Cree un programa que elimine todos los números impares de una list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("list original:", my_list)


my_list = [number for number in my_list if number % 2 == 0]

print("list modificada:", my_list)
