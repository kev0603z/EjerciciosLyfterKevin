#Cree una función que le dé la vuelta a un string y lo retorne.
#sto ya lo hicimos en iterables.
#Hola mundo” → “odnum aloH”


def reverse_string(text):
    invert = ""
    for letter in text:
        invert = letter + invert   
    return invert

print(reverse_string("Hello world"))
