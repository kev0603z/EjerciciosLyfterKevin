# python ejercicio5.py

counter_notes = 1
amount_approve_notes = 0
amount_disapprove_notes = 0
average_approve_notes = 0 
average_disapprove_notes = 0
all_notes = 0 
total_average_notes = 0

total_notes = int(input( " Digite la cantidad de notas que desea ingresar "))

while (counter_notes <= total_notes):
    
    current_note = int(input (f" Digite la nota {counter_notes} :   "))
    if current_note < 70:
        amount_disapprove_notes = amount_disapprove_notes + 1
        average_disapprove_notes = average_disapprove_notes + current_note
    else:
        amount_approve_notes = amount_approve_notes + 1
        average_approve_notes = average_approve_notes + current_note
    all_notes = all_notes + current_note    
    counter_notes = counter_notes + 1

if amount_disapprove_notes > 0:
    average_disapprove_notes = average_disapprove_notes / amount_disapprove_notes
else:
    average_disapprove_notes = 0

if amount_approve_notes > 0:
    average_approve_notes = average_approve_notes / amount_approve_notes
else:
    average_approve_notes = 0  

total_average_notes = all_notes // total_notes

print(f" El estudiante tiene esta cantidad de notas aprobadas: {amount_approve_notes}   ")
print(f" El promedio de notas aprobadas es de:  {average_approve_notes}   ")
print(f" El estudiante tiene esta cantidad de notas desaprobadas:  {amount_disapprove_notes}   ")
print(f" El promedio de notas desaprobadas es de:  {average_disapprove_notes}   ")
print(f" Este es el promedio total de las notas:  {total_average_notes}")




