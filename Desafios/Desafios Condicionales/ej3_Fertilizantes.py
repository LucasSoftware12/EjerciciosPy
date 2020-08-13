# Alumno Lucas Medina

tamañoCampo = int(
    input('\nIngrese el tamaño de su campo en metros cuadrados '))
matorral = int(input(
    '\n¿Su campo tiene matorral?'
    '\n 1: Si'
    '\n 2: No'
    '\n'))


if matorral == 1:
    print('No es factible usar fertilizantes.')

elif matorral == 2 and tamañoCampo*10/100 >= 1000:
    print('Es factible usar fertilizantes.')

else:
    print('No es factible usar fertilizantes.')
