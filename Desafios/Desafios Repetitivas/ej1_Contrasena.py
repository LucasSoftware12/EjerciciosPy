# Alumno Lucas Medina
user = input('\nUsuario:')
pw = input('\nContraseña: ')

i = 1

while(i < 3) & (pw != '123'):
    print('Contraseña Incorrecta')
    pw = input('\nIngrese Nuevamente: ')
    i += 1

if pw == '123':
    print('\nBienvenido', user)
else:
    print('\nCUENTA BLOQUEADA')
