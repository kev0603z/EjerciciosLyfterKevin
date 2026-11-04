import random

current_number = random.randint(1, 100)
number = 0
result = 0

def sum():
    try:
        number = int(input("Por favor digite el numero a sumar "))
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return current_number
    result = number + current_number
    print(f"La suma del numero {current_number} + {number} es: {result}")
    return result


def rest():
    try:
        number = int(input("Por favor digite el numero a restar "))
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return current_number
    result = current_number - number
    print (f" La resta del numero {current_number} - el numero {number} , es de : {result}")
    return result


def multiply():
    try:
        number = int(input("Por favor digite el numero a multiplicar "))
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return current_number
    result = number * current_number
    print (f" La multiplicacion del numero {current_number} * el numero {number} , es de : {result}")
    return result


def divide():
    try:
        number = int(input("Por favor digite el numero a dividir "))
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return current_number
    if number == 0:
        print("Error: no se puede dividir entre cero.")
        return current_number
    result = current_number / number
    print(f"La division del numero {current_number} / {number} es de: {result} ")
    return result


def menu():
    global current_number
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
            current_number = sum()
        elif option == 2:
            current_number = rest()
        elif option == 3:
            current_number = multiply()
            
        elif option == 4:
            current_number = divide()
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