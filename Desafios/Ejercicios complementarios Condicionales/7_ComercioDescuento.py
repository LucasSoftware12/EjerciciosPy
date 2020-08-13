# Alumno Lucas Medina

print("Ejercicio Descuento en comercio 15%")
compra = int(input("\n Ingrese monto de la compra: "))

if compra > 1000:
    descuento = (1000 * 15) / 100
    total = compra - descuento
    print(f"El descuento de 15% es de ${descuento}")
    print(f"El total a pagar es ${total}")

else:
    print(f"El total a pagar es ${compra}")
