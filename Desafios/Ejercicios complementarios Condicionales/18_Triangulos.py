# Alumno Lucas Medina


print("Ejercicio triangulos")

lado1 = int(input("Ingrese el lado 1: "))
lado2 = int(input("Ingrese el lado 2: "))
lado3 = int(input("Ingrese el lado 3: "))


if lado1 == lado2 == lado3:
    print("Triangulo Equilatero")

elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
    print("Triangulo isosceles")

elif lado1 != lado2 != lado3:
    print("Triangulo Escaleno")
