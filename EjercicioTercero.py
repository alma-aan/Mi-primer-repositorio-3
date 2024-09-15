print('=============================AULAS=============================')
while True: 
    dia = int(input('Ingrese el número del día 1 (lunes) a 6 (sábado): '))
    if 1 <= dia <= 6:
        break
    print('Por favor, ingrese un número entre 1 y 6.')

if dia %2 ==0:
    dia = 'A-300'
elif dia %2 == 1:
    dia ='A-315'
else:
    print('Número de día no válido') 

print(f'Aula: {dia}')

print('=========================Descuentos y Estacionamiento========================')
cuota = 7500
while True:
    turno = input('Ingrese el turno de cursada (Mañana, Tarde o Noche): ')
    if turno.lower() == 'mañana' or turno.lower() == 'tarde' or turno.lower() == 'noche':
        break
    print('Por favor, ingrese uno de los 3 turnos.')
materias = int(input('Ingrese la cantidad de materias: '))

if turno == 'tarde' and materias > 3:
    descuento = ((7500 * 25) / 100)
else:
    descuento = ((7500 * 5) / 100)
cuota_con_descuento = cuota - descuento
print('El valor de la cuota con descuento es de: ', cuota_con_descuento)

while True:
    estacionamiento = input('Ingrese el vehículo en el que ingresa(auto,moto,bicileta): ')
    if estacionamiento in ['auto', 'moto', 'bicicleta']:
        if estacionamiento.lower() == 'auto' or estacionamiento.lower() == 'moto':
            costo_estacionamiento = 300
        else: 
            costo_estacionamiento = 50
        print(f'El costo de estacionamiento para {estacionamiento.capitalize()} es de: ', costo_estacionamiento)
        break
    else:
        print('Por favor, ingrese un vehículo válido')
