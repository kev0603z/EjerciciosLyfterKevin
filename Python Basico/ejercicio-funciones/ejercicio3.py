#Cree una función que retorne la suma de todos los números de una list.
#La función va a tener un parámetro (la list) y retornar un número (la suma de todos sus elementos).
#[4, 6, 2, 29] → 41

def sum_list(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum

number = [4, 6, 2, 29]
print(sum_list(number)) 
