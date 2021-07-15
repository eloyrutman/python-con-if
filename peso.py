peso = 0.0

peso = float(input("Peso de la persona: "))

if peso >= 0:
    if peso <= 40:
        print ("Estatus: Flaco")
    elif peso <= 60:
        print("Estatus: Delgado")
    elif peso <= 80:
        print("Estatus: Rellenito")
    else:
        print("Estatus: Gordo")
else:
    print("Entrada Incorrecta")
print("Fin del Programa")

