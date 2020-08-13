# Alumno Lucas Medina
# Pizzas

Pizza = input("¿Quiere una Pizza vegetariana?")
if Pizza == "Si":
    Condimento = input("¿Quiere con Pimiento o Rúcula?")
    if Condimento == "Pimiento":
        Condimento = Condimento
    elif Condimento == "Rúcula":
        Condimento = Condimento
    else:
        print("No tenemos ese Condimento")
    print("La pizza es vegetariana con", Condimento)
if Pizza == "No":
    Condimento = input("¿Quiere con Jamón o Panceta?")
    if Condimento == "Jamón":
        Condimento = Condimento
    elif Condimento == "Panceta":
        Condimento = Condimento
    else:
        print("No tenemos ese Condimento")
    print("La pizza NO es vegetariana con", Condimento)
