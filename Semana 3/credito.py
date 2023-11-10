edad = int(input("Ingrese la edad: "))
antiguedad = int(input("Ingrese antiguedad: "))
ingreso = int(input("Ingrese salario: "))

if (edad >= 18) and (antiguedad >= 3) and (ingreso >= 2500):
    print("Se otorga el crédito")
elif (antiguedad < 3) and (ingreso >= 4000):
    print("Se otorga el crédito")
else:
    print("No se otorga el crédito")