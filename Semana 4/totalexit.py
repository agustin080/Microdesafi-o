cantidad = int(input("Ingrese la cantidad de números: "))
lista = []

for i in range(cantidad):
    numero = int(input("Ingresar numero: "))
    lista.append(numero)

promedio = sum(lista)/cantidad
print(promedio)