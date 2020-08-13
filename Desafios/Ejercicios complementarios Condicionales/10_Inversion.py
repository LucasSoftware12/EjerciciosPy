# Alumno Lucas Medina

print("Ejercicio Inversion")

inversion1 = int(input("Ingrese la primer inversion: "))
inversion2 = int(input("Ingrese la segunda inversion: "))
inversion3 = int(input("Ingrese la tercera inversion: "))


total = inversion1 + inversion2 + inversion3
inversion1Total = (inversion1/total)*100
inversion2Total = (inversion2/total)*100
inversion3Total = (inversion3/total)*100

print(f"Inversion Total: ${total} ")
print(f"Inversion del primero: %{inversion1Total} ")
print(f"Inversion del segundo: %{inversion2Total} ")
print(f"Inversion del tercero: %{inversion3Total} ")
