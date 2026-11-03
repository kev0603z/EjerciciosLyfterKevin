import random

def sum(current_number):
    number = get_number("Digite el número a sumar: ")
    if number is None:
        return current_number

    return current_number + number


def rest(current_number):
    number = get_number("Digite un número: ")

    if number is None:
        return current_number

    return current_number - number


def multiply(current_number):

    number = get_number("Digite un número: ")
    
    if number is None:
        return current_number
    
    return current_number * number


def divide( current_number):
    number = get_number("Digite el número a dividir: ")

    if number is None:
        return current_number

    try:
        return current_number / number
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
        return current_number


def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return None


def menu():
    current_number = random.randint(1, 100)
    while True:
        print(f"\nNúmero actual: {current_number}")

        print(
            " *  Calculadora  *\n"
            " |  1. Sumar            |\n"
            " |  2. Restar           |\n"
            " |  3. Multiplicar      |\n"
            " |  4. Dividir          |\n"
            " |  5. Borrar resultado |\n"
            " |  6. Salir |\n"
        )

        try:
            option = int(input("Digite el numero del menu (1-6): "))
        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        if option == 1:
            current_number = sum(current_number)
        elif option == 2:
            current_number = rest(current_number)
        elif option == 3:
            current_number = multiply(current_number)
            
        elif option == 4:
            current_number = divide(current_number)
        elif option == 5:
            current_number = 0
            print("Resultado borrado.")
        elif option == 6:
            print (" Saliendo del programa ...")
            break
        else:
            print ("   ")
            print (" Opción inválida ")
menu()