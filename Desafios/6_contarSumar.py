while True:
    x = int(input("Ingrese el primer numero: "))
    z = int(input("Ingrese el segundo numero: "))
    if z < x:
        print("El segundo numero debe ser mayor al primero, vuelva a ingresarlo")
        z = int(input("Ingrese el segundo numero: "))
    elif z >= x:
        break

cont = 0
cont2 = 0

for i in range(x, z+1, 1):
    if i % 2 == 0:
        cont += 1
        print("Multiplo N°", cont, "es:", i)
        cont2 += i

print("Hay", cont, "multiplos de 2 entre esos 2 numeros")
print("La suma de los multiplos de 2 es:", cont2)
