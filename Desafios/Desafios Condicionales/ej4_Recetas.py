# Alumno Lucas Medina
receta1 = ["Lentejas", "Apio", "Verduras", "Berenjena"]
receta2 = ["Morrón", "Cebolla", "Verduras", "Berenjena"]
recetaFinal = []
cantidad = 0

tipo = int(input(
    '\n¿Que tipo de receta desea?'
    '\n 1: Receta 1'
    '\n 2: Receta 2'
    '\n'))

if tipo == 1:
    tipo = "Receta 1"
    for i in receta1:
        if cantidad <= 2:
            print('1 = Si y 0 = No\n')
            eleccion = int(input(i))
        if eleccion == 1:
            recetaFinal.append(i)
            cantidad = cantidad+1
elif tipo == 2:
    tipo = "Receta 2"
    for i in receta2:
        if cantidad <= 2:
            print('1 = Si y 0 = No\n')
            eleccion = int(input(i))
        if eleccion == 1:
            recetaFinal.append(i)
            cantidad = cantidad+1


print('Elegíste la', tipo, 'con', recetaFinal)
