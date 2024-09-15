# Número total de días que deseas mostrar
num_dias = 6

# Aulas a utilizar
aula_par = "A-300"
aula_impar = "A-315"

# Imprimir el encabezado del listado
print("Día\tAula")

# Iterar sobre los días
for dia in range(1, num_dias + 1):
    # Determinar el aula según si el día es par o impar
    aula = aula_par if dia % 2 == 0 else aula_impar
    print(f"{dia}\t{aula}")