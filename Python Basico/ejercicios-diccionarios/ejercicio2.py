## 2. Cree un programa que cree un diccionario usando dos lists del mismo tamaño, usando una para sus keys, y la otra para sus values.

list_a = ["first_name ", "last_name ", "role "]
list_b = ["Kevin", "Zuniga", "Software Engineer"]

dict = {}
for index in range(len(list_a)):
    dict[list_a[index]] = list_b[index]

print(dict)

