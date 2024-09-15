nota1 = float(input('Ingrese nota del primer examen: '))
nota2 = float(input('Ingrese nota del segundo examen: '))
promedio = (nota1 + nota2) / 2

print('')
print('===================Programa de Resultados de Notas============================= \n')
print(f'El promedio de las notas es:  {promedio:.2f}\n')
if nota2 >= 7:
    print('Aprobó el segundo examen')
else: 
    print('No aprobó el segundo examen')
print('Progreso del 1er al 2do parcial: ')
if nota1 == nota2:
    print('Mantuvo su desempeño')
elif nota1 < nota2:
    print('Mejoró su desempeño')
else:
    print('Empeoró su desempeño')
if promedio >= 4:
    print('El alumno promocionó la materia')
else:
    print('El alumno debe recursar la materia')
