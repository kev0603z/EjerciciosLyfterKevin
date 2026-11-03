#Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a list, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


def order_string(text):
    list = text.split("-")
    list.sort()
    result = "-".join(list)
    return result

text = "python-variable-funcion-computadora-monitor"
print(order_string(text))
