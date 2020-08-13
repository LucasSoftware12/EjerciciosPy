# Alumno Lucas Medina

print("Ejercicio Número mayor")
numUno = int(input("Ingrese un numero: "))
numDos = int(input("Ingrese un numero: "))
numTres = int(input("Ingrese un numero: "))

if (numUno > numDos) and (numUno > numTres):
    print(f"El numero mayor es: {numUno}")

elif (numDos > numUno) and (numDos > numTres):
    print(f"El numero mayor es: {numDos}")

elif (numTres > numDos) and (numTres > numUno):
    print(f"El numero mayor es: {numTres}")
