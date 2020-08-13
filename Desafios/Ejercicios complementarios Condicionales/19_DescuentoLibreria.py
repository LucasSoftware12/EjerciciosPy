# Alumno Lucas Medina

print("Ejercicio libreria")

cantidadLibros = int(input("Ingrese la cantidad: "))
tipo = int(input("Ingrese que tipo de cliente es:"
                 "\n1: libreria"
                 "\n2: particular"
                 "\n "))
importe = int(input("Ingrese el importe total para calcular descuento: "))


if cantidadLibros <= 24 and tipo == 1:
    descuento = importe * 20 / 100
    totalFinal = importe - descuento
    print(
        f"El importe final a pagar es: ${totalFinal} menos descuento del 20%")

elif cantidadLibros > 24 and tipo == 1:
    descuento = importe * 25 / 100
    totalFinal = importe - descuento
    print(
        f"El importe final a pagar es: ${totalFinal} menos descuento del 25%")

elif cantidadLibros == 6 and tipo == 2:
    print(f"Total a pagar es: ${importe}")

elif cantidadLibros > 6 and cantidadLibros <= 18 and tipo == 2:
    descuento = importe * 5 / 100
    totalFinal = importe - descuento
    print(f"El importe final a pagar es: ${totalFinal} menos descuento del 5%")

elif cantidadLibros > 18 and tipo == 2:
    descuento = importe * 10 / 100
    totalFinal = importe - descuento
    print(
        f"El importe final a pagar es: ${totalFinal} menos descuento del 10%")
