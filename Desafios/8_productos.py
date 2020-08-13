# Alumno Lucas Medina
# Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.

total = 0

while True:
    cantidad = int(input("Ingrese la cantidad de productos: "))
    valor = int(input("Ingrese el precio del producto: "))

    total1 = cantidad*valor
    print(f"El total de estos productos es {total1}")

    total += total1

    continuar = int(input("¿Desea añadir más productos?"
                          "\n 1) SI: "
                          "\n 2) NO: "))
    if continuar == 2:
        print(f"El total es {total}")
        break
    elif continuar == 1:
        continue
