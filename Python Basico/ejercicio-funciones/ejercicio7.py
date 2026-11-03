#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a #código. No busque el código, eso no ayudaría.
#Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar otra función para revisar si el numero es primo o no.

def prime_number(number):
    if number <= 1:   
        return False
    for index in range(2, int(number**0.5) + 1): 
        if number % index == 0:   
            return False
    return True


def filter_prime(list):
    prime = []
    for number_list in list:       
        if prime_number(number_list):     
            prime.append(number_list) 
    return prime 


number_list = [1, 4, 6, 7, 13, 9, 67]
print(filter_prime(number_list))

