from actions import students
import actions
import csv


def export_students(students):

    if len(students) == 0:
            print("No hay estudiantes para exportar.")
            return

    file = open("students.csv", "w", newline="")
    writer = csv.writer(file)

    writer.writerow([
        "name",
        "section",
        "spanish_grade",
        "english_grade",
        "socials_grade",
        "science_grade"
    ])

    for student in students:

        writer.writerow([
            student["name"],
            student["section"],
            student["spanish_grade"],
            student["english_grade"],
            student["socials_grade"],
            student["science_grade"]
        ])

    file.close()

    print("\nEstudiantes exportados correctamente. !!!")





import csv

def import_students():

    students = []

    try:

        file = open("students.csv", "r")
        reader = csv.DictReader(file)

        for row in reader:

            student = {
                "name": row["name"],
                "section": row["section"],
                "spanish_grade": float(row["spanish_grade"]),
                "english_grade": float(row["english_grade"]),
                "socials_grade": float(row["socials_grade"]),
                "science_grade": float(row["science_grade"])
            }

            students.append(student)

        file.close()
        print("Estudiantes importados correctamente.")
        return students
    except FileNotFoundError:

        print("No se encontro registro.")
        return []

