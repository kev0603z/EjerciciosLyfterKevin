#3. Cree un programa que use una list para eliminar keys de un diccionario.

list_of_keys = ["access_level", "age"]
employee = {"name": "kevin", "email": "kev@gmail.com", "access_level": 7, "age": 23}
print(" Diccionario original : ", employee)

for key in list_of_keys:
    employee.pop(key) 
print(" Diccionario sin list de keys : ", employee)
