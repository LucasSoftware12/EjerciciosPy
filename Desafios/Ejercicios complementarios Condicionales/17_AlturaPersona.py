# Alumno Lucas Medina


print("Ejercicio altura persona")

estatura = int(input("Ingrese su altura en centimetros "))
sexo = int(input("Ingrese su sexo:"
                 "\n 1= Masculino"
                 "\n 2= Femenino"
                 "\n "))


if estatura <= 165 and sexo == 1:
    print(f"Su estatura '{estatura}' esta por debajo de la media de su sexo")

elif estatura <= 175 and sexo == 2:
    print(f"Su estatura '{estatura}' esta por debajo de la media de su sexo")
elif estatura > 175 and sexo == 2:
    print(f"Su estatura '{estatura}' esta por encima de la media de su sexo")

elif estatura > 165 and sexo == 1:
    print(f"Su estatura '{estatura}' esta por encima de la media de su sexo")
