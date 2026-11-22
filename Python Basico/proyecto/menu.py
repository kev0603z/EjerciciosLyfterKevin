import actions
import data


def menu(students):
    
    while True:
        
        print(
                    " *      Sistema de registro     *\n"
                    " |  1. Registrar estudiantes     |\n"
                    " |  2. Ver estudiantes           |\n"
                    " |  3. Top 3 promedios           |\n"
                    " |  4. Promedio General          |\n"
                    " |  5. Exportar                  |\n"
                    " |  6. Importar                  |\n"
                    " |  7. Salir                     |\n"
        )

        try:
            option = int(input("Digite el numero del menu (1-7): "))
        except ValueError:
            print("Error: debe ingresar un número.")
            continue
        

        
        match option:

                case 1:
                    actions.add_students(students)
                    
                case 2:
                    actions.show_students(students)
                    
                case 3:
                    actions.show_top_3(students)
                    
                case 4:
                    actions.show_general_average(students)
                        
                case 5:
                    
                    data.export_students(students)
                case 6:
                    
                    students = data.import_students()
                case 7:
                    print(" Saliendo ...")
                    break
                    
                case _:
                    print(" Seleccione un numero del menu")
                    





