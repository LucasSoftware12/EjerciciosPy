# Alumno Lucas Medina


print("Ejercicio Descuento")


producto = input("Ingrese Nombre del Producto: ")
precio = int(input("Ingrese el precio: "))
clave = int(input("Ingrese la clave del producto: "))

if clave == 1:
    descuento = (precio * 10)/100
    precioDescuento = precio - descuento
    print(
        f"\n Producto: {producto}, Total a pagar: ${precioDescuento} con un descuento del 10%")
elif clave == 2:
    descuento = (precio * 20)/100
    precioDescuento = precio - descuento
    print(
        f"\n Producto: {producto}, Total a pagar: ${precioDescuento} con un descuento del 20%")

else:
    print(f"Total a pagar: ${precio}")
