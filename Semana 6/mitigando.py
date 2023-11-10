def dividir(a,b):
    try:
        return print("El cociente es: ", a/b)
    except:
            print("No se puede dividir por 0.")

a = int(input("Ingrese un valor: "))
b = int(input("Ingrese un valor: "))

dividir(a,b)


