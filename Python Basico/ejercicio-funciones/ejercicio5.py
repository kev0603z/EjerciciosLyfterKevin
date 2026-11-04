#Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def count_letter(text):
    upper_cases = 0
    lower_cases = 0

    for char in text:
        if char.isupper():
            upper_cases += 1
        elif char.islower():
            lower_cases += 1

    return upper_cases, lower_cases

text = "YO amo la Liga Deportiva Alajuelence"
mayus, minus = count_letter(text)
print(f"There’s {mayus} upper cases and {minus} lower cases")
