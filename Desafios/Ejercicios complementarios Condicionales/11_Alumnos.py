# Alumno Lucas Medina

print("Ejercicio Alumnos")

calificacion1 = int(input("Ingrese primera calificacion: "))
calificacion2 = int(input("Ingrese segunda calificacion: "))
calificacion3 = int(input("Ingrese tercera calificacion: "))


calificacionTotal = calificacion1 + calificacion2 + calificacion3
promedioTotal = calificacionTotal/3


if promedioTotal >= 70:
    print(f"Promedio de {promedioTotal} : Aprobado")
elif promedioTotal < 70:
    print(f"Promedio de {promedioTotal} : Desaprobado")
