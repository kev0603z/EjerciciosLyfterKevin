

def get_text(prompt):

    while True:

        text = input(prompt).strip()
        if text == "":
            print("Error: no puede dejar el campo vacío.")
        elif text.isdigit():
            print("Error: debe ingresar texto y no números.")
        else:
            return text

def get_grade(prompt):

    while True:
        try:
            grade = float(input(prompt))
        except ValueError:
            print("Error: debe ingresar un número.")
            continue
        if grade < 0 or grade > 100:
            print("Error: la nota debe estar entre 0 y 100.")
        else:
            return grade


def get_student_amount():

    while True:
        try:
            amount = int(input("¿Cuántos estudiantes desea registrar? "))

            if amount <= 0:
                print("Error: debe ingresar un número mayor que 0.")
                continue

            return amount

        except ValueError:
            print("Error: debe ingresar un número entero.")

def create_student():

    name = get_text("Nombre del Estudiante: ")
    section = get_text(" Seccion:  ")

    spanish_grade = get_grade(" Nota de Español : ")
    english_grade = get_grade(" Nota de Ingles : ")
    socials_grade = get_grade(" Nota de Sociales : ")
    science_grade = get_grade(" Nota de Ciencias : ")

    return {
        "name": name,
        "section": section,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "socials_grade": socials_grade,
        "science_grade": science_grade,
    }

def add_students(students):
    amount_students = get_student_amount()
    for index in range(amount_students):
        print(f"\nEstudiante #{index + 1}")
        student = create_student()
        students.append(student)
        
        
def show_students(students):

    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return 

    for student in students:
        print("\n-------------------------")
        print(f"Nombre: {student['name']}")
        print(f"Sección: {student['section']}")
        print(f"Nota Español: {student['spanish_grade']}")
        print(f"Nota Inglés: {student['english_grade']}")
        print(f"Nota Sociales: {student['socials_grade']}")
        print(f"Nota Ciencias: {student['science_grade']}")
        average = calculate_average(student)
        print(f" Promedio :" , average)
        print("-------------------------")


def calculate_average(student):

    average =((student["spanish_grade"] + 
               student['english_grade'] + 
               student['socials_grade']+
               student['science_grade'] ) /4.)
    return average


def show_general_average(students):

    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return
    
    total_average = 0

    for student in students:
        total_average += calculate_average(student)
    general_average = total_average / len(students)
    print(f"Promedio General: {general_average}")
    

def show_top_3(students):
    if len(students) == 0:
        print("No hay estudiantes registrados.")
        return
    
    top_students = sorted(
        students,
        key=calculate_average,
        reverse=True
    )[:3]

    print("\n===== TOP 3 DE ESTUDIANTES =====")

    for position, student in enumerate(top_students, start=1):
        average = calculate_average(student)

        print(f"\nPuesto #{position}")
        print(f"Nombre: {student['name']}")
        print(f"Sección: {student['section']}")
        print(f"Promedio: {average:.2f}")


