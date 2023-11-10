def anio_bisiesto(anio):
    if type(anio) != int:
        print("Ingrese un número válido.")
    else:
        if (anio % 4 == 0 or anio % 400 == 0) and anio % 100 != 0:
            print(anio, "es un año bisiesto.")
        else:
            print(anio, "no es un año bisiesto.")
    return

anio_bisiesto(1998)
anio_bisiesto(2012)
anio_bisiesto(1997)