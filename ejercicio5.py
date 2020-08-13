# Alumno Lucas Medina
# Turnos

inicial = input("Ingrese la primer letra de su apellido: ")
turno = input("Ingrese su turno: ")

if inicial == "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M":
    if turno == "Tarde":
        print("Perteneces al grupo A")
    elif turno == "Noche":
        print("Perteneces al grupo B")
        
elif inicial == "N" or "Ñ" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z":
    if turno == "Tarde":
        print("Perteneces al Grupo A")
    elif turno == "Noche":
        print("Perteneces al grupo B")
