# Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. Desea obtener de todas las personas que alcance a encuestar en un día, que porcentaje tiene estudios de primaria, secundaria, carrera técnica, estudios profesionales y estudios de posgrado.
inicio = True
primaria = 0
secundaria = 0
carrera = 0
profesionales = 0
posgrado = 0

while inicio:
    print('Campaña de senso')
    estudios = int(input('Tiene estudios primarios? '
                         '1) Si'
                         '2) No'))
    if estudios == 1:
        primaria = primaria+1

    estudios1 = int(input('Tiene estudios secundarios? '
                          '1) Si'
                          '2) No'))
    if estudios1 == 1:
        secundaria = secundaria+1

    estudios2 = int(input('Tiene carrera técnica? '
                          '1) Si'
                          '2) No'))
    if estudios2 == 1:
        carrera = carrera+1

    estudios3 = int(input('Tiene estudios profesionales? '
                          '1) Si'
                          '2) No'))
    if estudios3 == 1:
        profesionales = profesionales+1

    estudios4 = int(input('Tiene estudios posgrado? '
                          '1) Si'
                          '2) No'))
    if estudios4 == 1:
        posgrado = posgrado+1
    personas = primaria+secundaria+carrera+profesionales+posgrado

    seguimos = (input('\nSeguimos'
                      '\nSi''\nNo'
                      '\n'))

    if seguimos == "No":
        inicio = False
    print('cantidad de personas', personas)
    print('Porcentaje de personas que tiene estudios primarios %',
          (primaria/personas)*100)
    print('Porcentaje de personas que tiene estudios secundaria %',
          (secundaria/personas)*100)
    print('Porcentaje de personas que tiene carrera tecnica %',
          (carrera/personas)*100)
    print('Porcentaje de personas que tiene estudios profesionales %',
          (profesionales/personas)*100)
    print('Porcentaje de personas que tiene estudios posgrado %',
          (posgrado/personas)*100)
