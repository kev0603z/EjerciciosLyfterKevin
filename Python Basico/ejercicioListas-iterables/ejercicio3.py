# python ejercicio3.py
# Cree un programa que intercambie el primer y ultimo elemento de una list. Debe funcionar con lists de cualquier tamaño.

country_list = ['panama', 'nicaragua', 'honduras', 'costa rica']

print("list original:", country_list)

country_list[0], country_list[-1] = country_list[-1], country_list[0]

print( " list modificada:" , country_list)
