annio = int(input("Ingrese un año: "))
if (annio % 4 == 0 and annio % 100 != 0) or annio % 400 == 0:
    print("El año ", annio, "Si es Bisiesto")

else:
    print("El año ", annio, "No es Bisiesto")