# Alumno Lucas Medina
inicio = True
personas = 0
menos100 = 0
menos200 = 0
mas200 = 0

while inicio:
    print('Campaña de recolección')
    colillas = int(input('Ingrese la cantidad de colillas: '))
    if colillas < 100:
        menos100 = menos100+1
    elif colillas < 200:
        menos200 = menos200+1
    else:
        mas200 = mas200+1
    personas = menos100+menos200+mas200
    seguimos = int(input('\nSeguimos''\n1= Si''\n0= No''\n'))
    if seguimos == 0:
        inicio = False
print('cantidad de personas', personas)
print('Menos 100 colillas %', (menos100/personas)*100)
print('Menos 200 colillas %', (menos200/personas)*100)
print('Más 200 colillas %', (mas200/personas)*100)
