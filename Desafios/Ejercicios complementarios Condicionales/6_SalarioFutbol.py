# Alumno Lucas Medina

print("Ejercicio aumento de salarios")
sueldo = int(input("Ingrese su sueldo: "))


if sueldo > 0 and sueldo < 6000:
    aumento = ((sueldo * 15) / 100) + sueldo
    print(f"Sueldo Actualizado ${aumento}")

elif sueldo > 6000 and sueldo < 7900:
    aumento = ((sueldo * 10) / 100) + sueldo
    print(f"Sueldo Actualizado ${aumento} ")


elif sueldo > 7900 and sueldo < 12000:
    aumento = ((sueldo * 6) / 100) + sueldo
    print(f"Sueldo Actualizado ${aumento} ")

elif sueldo > 12000:
    print("El sueldo no tiene aumento")
