# 1) Determinar el número mayor de 10 números ingresados.
mayor = 0
maximo = 10

for i in range(maximo):
    num = int(input('Dame un numero: '))
    if num > mayor:
        mayor = num

print(f"El mayor de los 10 numeros es: {mayor}")
