def promedio(args):
    sum(args)/len(args)
    return print("El promedio es: ", sum(args)/len(args))

lista = []

while True:
    numero = input("Ingresar un número: ")
    if numero.lower() == "exit":
        break

    else:
        numeros = int(numero)
        lista.append(numeros)

promedio(lista)

