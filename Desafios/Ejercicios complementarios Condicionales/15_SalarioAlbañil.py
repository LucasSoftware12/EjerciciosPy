# Alumno Lucas Medina


print("Ejercicio salario albañil")

horas = int(input("\nIngrese cantidad de horas: "))


if horas <= 40:
    bono = horas * 16
    print(f"La bonificacion por hora de trabajo es:${bono}")

elif horas > 40:
    bono = 40 * 16
    bonoExtra = (horas/40) * 20
    bonoFinal = bono + bonoExtra
    print(f"La bonificacion por horas extras es: $ {bonoExtra}")
    print(f"La bonificacion por horas de trabajo es:$ {bonoFinal}")
