# Alumno Lucas Medina

print("Ejercicio Triangulos")

ladoUno = int(input("\n Ingrese longitud de lado 1: "))
ladoDos = int(input("\n Ingrese longitud de lado 2: "))
ladoTres = int(input("\n Ingrese longitud del lado 3: "))


if ladoUno >= ladoDos + ladoTres:
    print("Las longitudes ingresadas no corresponden a un triangulo")

elif ladoUno ** ladoUno == (ladoDos ** ladoDos) + (ladoTres ** ladoTres):
    print("\n Triangulo Rectangulo")

elif ladoUno ** ladoUno > (ladoDos ** ladoDos) + (ladoTres ** ladoTres):
    print("\n Triangulo obtusangulo")

elif ladoUno ** ladoUno < (ladoDos ** ladoDos) + (ladoTres ** ladoTres):
    print("\n Triangulo acutangulo")
