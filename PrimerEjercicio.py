nombre = input('Ingrese su nombre completo: ')
edad = int(input('Ingrese su edad: '))
fecha = input('Ingrese su fecha de nacimiento: ')
matricula = int(input('ingrese la matricula: '))
titulo = True

cuota = matricula + 1000
arancel = 12000 /4 
descuento = arancel - ((arancel * 15) / 100) 

print('===================================================================================================== ')
print('===========================Universidad de Pyhton - Inscripciones===================================== ')
print('===================================================================================================== \n')

print('Nombre completo: ', nombre)
print(f'Fecha de nacimiento: {fecha}, ({edad}')
print('Matrícula: ', matricula)
print('¿Posee título secundario?: ', titulo)
print('La cuota mensual es de: ', cuota)
print('El arancel mensual de la materia Python I es de: ', arancel)
print('El arancel mensual de la materia Python I con el descuento del 15%:  ', descuento) 
