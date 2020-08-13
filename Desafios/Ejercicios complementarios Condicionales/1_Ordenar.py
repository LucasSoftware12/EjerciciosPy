# Alumno Lucas Medina

print("Ejercicio de mayor a menor")
numUno = int(input("\n Ingrese un número: "))
numDos = int(input("\n Ingrese número: "))
numTres = int(input("\n Ingrese número: "))


if numUno > numDos and numUno > numTres:
    print(f'De mayor a menor: {numUno}, {numDos}, {numTres}')


elif numDos > numTres and numDos > numUno:
    print(f'De mayor a menor: {numDos}, {numTres}, {numUno}')

elif numDos > numUno and numDos > numTres:
    print(f'De mayor a menor: {numDos}, {numUno}, {numTres}')


elif numTres > numDos and numTres > numUno:
    print(f'De mayor a menor: {numTres}, {numDos}, {numUno}')
