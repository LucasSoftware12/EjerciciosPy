# Alumno Lucas Medina


print("Ejercicio descuento camisas")


cantidad = int(input("Ingrese la cantidad de camisas: "))
precio = int(input("Ingrese el precio: "))


if cantidad > 3:
    total = precio * 20 / 100
    descuento = precio - total
    print(f"Total a pagar: ${descuento} con un descuento del 20%")
elif cantidad < 3:
    total = precio * 10 / 100
    descuento = precio - total
    print(f"Total a pagar: ${descuento} con un descuento del 10%")
