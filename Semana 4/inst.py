lista = list(range(1,101,2))
print(lista)
suma = sum(lista)
print(suma)

numero = int(input("Ingrese un número del 0 al 9: "))
if numero <= 9:
    if numero in lista:
        print("Valor en lista")
    else:
        print("El número no está en la lista")
else:
    print("Número incorrecto")