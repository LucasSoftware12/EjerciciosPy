# Alumno Lucas Medina


print("Ejercicio Descuento azar")

precio = int(input("Ingrese el precio del producto: "))
azar = int(input("Elija un numero del 1 al 100: "))


if azar < 74:
    descuento = precio * 15 / 100
    precioFinal = precio - descuento
    print(f"Total a pagar es: ${precioFinal} con un descuento del 15%")
elif azar >= 74:
    descuento = precio * 20 / 100
    precioFinal = precio - descuento
    print(f"Total a pagar es: ${precioFinal} con un descuento del 20%")
