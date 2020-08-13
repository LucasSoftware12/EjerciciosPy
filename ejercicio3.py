# Alumno Lucas Medina
# Ventas del día

ventasDiaUno = int(input("Ingrese las ventas del Dia uno: "))
# print(ventasDiaUno)
ventasDiaDos = int(input("Ingrese las ventas del Dia dos: "))
# print(ventasDiaDos)

if ventasDiaUno > ventasDiaDos:
    print("Se vendió más en el día uno")
elif ventasDiaUno == ventasDiaDos:
    print("Vendieron lo mismo en ambos días")
else:
    print("Se vendió más en el día dos")
