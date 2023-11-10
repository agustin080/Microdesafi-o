cantidad = int(input("Ingrese la cantidad de números: "))
lista = []
numeros_ingresados = 0
suma = 0

#while numeros_ingresados <= cantidad:
for i in range(cantidad):
    numero = input("Ingrese un numero: ")
    if numero != "exit":
        numeros_ingresados += 1
        suma += int(numero)
    else:
        print("La carga de datos fue parcial y el promedio es: ", suma/numeros_ingresados)
        
print(numeros_ingresados)
promedio = suma/cantidad
print("La carga de datos fue total y el promedio es: ", promedio)

