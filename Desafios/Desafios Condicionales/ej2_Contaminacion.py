# Alumno Lucas Medina

tamaño = input(
    '\nElija el tamaño del pez:'
    '\n 1: Normal'
    '\n 2: Por debajo de lo normal'
    '\n 3: Por encima de lo normal'
    '\n 4: Sobredimensionado'
    '\n')

if tamaño == '1':
    print('Pez en buenas condiciones')
elif tamaño == '2':
    print('Pez con problemas de nutrición')
elif tamaño == '3':
    print('Pez con síntomas de organismo contaminado')
elif tamaño == '4':
    print('Pez contaminado')
