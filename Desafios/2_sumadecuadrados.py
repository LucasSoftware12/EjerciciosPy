# 2) Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.

num = int(input("Ingrese hasta que numero sumar"))
suma = 0

for i in range(num+1):
    suma += i**2
print(
    f"La suma de los anteriores de {num} primeros numeros naturales es {suma}")
