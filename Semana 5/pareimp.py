pares = []
impares = []

def ordenar(numero2):
    if numero2 % 2 == 0:
        pares.append(numero2)
    if numero2 % 2 != 0:
        impares.append(numero2)
    return

while True:    
    numero = input("Ingrese un número: ")
    if numero.lower() == "exit":
        break
    numero2 = int(numero)
    ordenar(numero2)

pares.sort()
impares.sort()
print(pares)
print(impares)