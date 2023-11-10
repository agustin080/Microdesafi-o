nombre = input("Ingrese un nombre: ")
edad = int(input("Ingrese una edad: "))

if (nombre != "****") and (edad > 5) and (edad < 20) and (4<= len(nombre) < 8) and (edad * 3 > 35):
    print("La edad y el nombre ingresados cumplen con las condiciones.")
else: 
    print("La edad y el nombre ingresados no cumplen con las condiciones")