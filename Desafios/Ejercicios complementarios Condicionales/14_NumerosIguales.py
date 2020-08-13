# Alumno Lucas Medina


print("Ejercicio numeros iguales")


num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingresse segundo numero: "))

if num1 == num2:
    num3 = num1 * num2
    print(f"El producto de los numeros iguales es: {num3}")
elif num1 > num2:
    num3 = num1 - num2
    print(f"La resta de los numeros: {num3}")
else:
    num3 = num1 + num2
    print(f"La suma de los numeros distintos es: {num3}")
